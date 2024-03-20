# Copyright (c) 2022 The BayesFlow Developers

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import logging
import os
from pickle import load as pickle_load

import numpy as np
import tensorflow as tf
from tqdm.autonotebook import tqdm

from bayesflow.amortizers import (
    AmortizedLikelihood,
    AmortizedModelComparison,
    AmortizedPosterior,
    AmortizedPosteriorLikelihood,
)
from bayesflow.computational_utilities import maximum_mean_discrepancy
from bayesflow.configuration import *
from bayesflow.default_settings import DEFAULT_KEYS, OPTIMIZER_DEFAULTS, TQDM_MININTERVAL
from bayesflow.diagnostics import plot_latent_space_2d, plot_sbc_histograms
from bayesflow.exceptions import ArgumentError, SimulationError
from bayesflow.helper_classes import (
    EarlyStopper,
    LossHistory,
    MemoryReplayBuffer,
    MultiSimulationDataset,
    SimulationDataset,
    SimulationMemory,
)
from bayesflow.helper_functions import backprop_step, extract_current_lr, format_loss_string, loss_to_string
from bayesflow.simulation import GenerativeModel, MultiGenerativeModel

logging.basicConfig()


class Trainer:
    """This class connects a generative model (or, already simulated data from a model) with
    a configurator and a neural inference architecture for amortized inference (amortizer). A Trainer
    instance is responsible for optimizing the amortizer via various forms of simulation-based training.

    At the very minimum, the trainer must be initialized with an `amortizer` instance, which is capable
    of processing the (configured) outputs of a generative model. A `configurator` will then process
    the outputs of the generative model and convert them into suitable inputs for the amortizer. Users
    can choose from a palette of default configurators or create their own configurators, essentially
    building a modularized pipeline `GenerativeModel` -> `Configurator` -> `Amortizer`. Most complex models
    will require custom configurators.

    Notes
    -----

    Currently, the trainer supports the following simulation-based training regimes, based on efficiency
    considerations:

    * Online training

      >>> trainer.train_online(epochs, iterations_per_epoch, batch_size, **kwargs)

      This training regime is optimal for fast generative models which can efficiently simulated data on-the-fly.
      In order for this training regime to be efficient, on-the-fly batch simulations should not take longer
      than 2-3 seconds.

    * Experience replay training

      >>> trainer.train_experience_replay(epochs, iterations_per_epoch, batch_size, **kwargs)

      This training regime is also good for fast generative models capable of efficiently simulating data on-the-fly.
      Compare to pure online training, this training will keep an experience replay buffer from which simulations
      are randomly sampled, so the networks will likely see some simulations multiple times.

    * Round-based training

      >>> trainer.train_rounds(rounds, sim_per_round, epochs, batch_size, **kwargs)

      This training regime is optimal for slow, but still reasonably performant generative models.
      In order for this training regime to be efficient, on-the-fly batch simulations should not take
      longer than 2-3 minutes.

      .. note:: overfitting presents a danger when using small numbers of simulated data sets, so it is recommended
         to use some amount of regularization for the neural amortizer(s).

    * Offline training

      >>> trainer.train_offline(simulations_dict, epochs, batch_size, **kwargs)

      This training regime is optimal for very slow, external simulators, which take several minutes for a
      single simulation. It assumes that all training data has been already simulated and stored on disk.

      .. warning:: Overfitting presents a danger when using a small simulated data set, so it is recommended to use
         some amount of regularization for the neural amortizer(s).

      .. note::
         For extremely slow simulators (i.e., more than an hour of a single simulation), the BayesFlow framework
         might not be the ideal choice and should probably be considered in combination with a black-box surrogate
         optimization method, such as Bayesian optimization.

    """

    def __init__(
        self,
        amortizer,
        generative_model=None,
        configurator=None,
        checkpoint_path=None,
        max_to_keep=3,
        default_lr=0.0005,
        skip_checks=False,
        memory=False,
        **kwargs,
    ):
        """Creates a trainer which will use a generative model (or data simulated from it) to optimize
        a neural architecture (amortizer) for amortized posterior inference, likelihood inference, or both.

        Parameters
        ----------
        amortizer         : `bayesflow.amortizers.Amortizer`
            The neural architecture to be optimized.
        generative_model  : `bayesflow.forward_inference.GenerativeModel`
            A generative model returning a dictionary with randomly sampled parameters, data, and optional context
        configurator      : callable or None, optional, default: None
            A callable object transforming and combining the outputs of the generative model into inputs for a BayesFlow
            amortizer.
        checkpoint_path   : string or None, optional, default: None
            Optional file path for storing the trained amortizer, loss history and optional memory.
        max_to_keep       : int, optional, default: 3
            Number of checkpoints and loss history snapshots to keep.
        default_lr        : float, optional, default: 0.0005
            The default learning rate to use for default optimizers.
        skip_checks       : bool, optional, default: False
            If True, do not perform consistency checks, i.e., simulator runs and passed through nets
        memory            : bool or bayesflow.SimulationMemory, optional, default: False
            If ``True``, store a pre-defined amount of simulations for later use (validation, etc.).
            If `SimulationMemory` instance provided, stores a reference to the instance.
            Otherwise the corresponding attribute will be set to None.

        Other Parameters:
        -----------------

        memory_kwargs : dict
           Keyword arguments to be passed to the `SimulationMemory` instance, if ``memory=True``
        num_models : int
           The number of models in an amortized model comparison scenario, in case of a custom model comparison
           amortizer which does not have a num_models attribute.

        """

        # Set-up logging
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        self.amortizer = amortizer
        self.generative_model = generative_model
        if self.generative_model is None:
            logger.info(
                "Trainer initialization: No generative model provided. Only offline learning mode is available!"
            )

        # Determine n models in case model comparison mode
        if type(generative_model) is MultiGenerativeModel:
            _num_models = generative_model.num_models
        elif type(amortizer) is AmortizedModelComparison:
            _num_models = amortizer.num_models
        else:
            _num_models = kwargs.get("num_models")

        # Set-up configurator
        self.configurator = self._manage_configurator(configurator, num_models=_num_models)

        # Set-up memory classes
        self.loss_history = LossHistory()
        if memory is True:
            self.simulation_memory = SimulationMemory(**kwargs.pop("memory_kwargs", {}))
        elif type(memory) is SimulationMemory:
            self.simulation_memory = memory
        else:
            self.simulation_memory = None

        # Set-up replay buffer and optimizer attributes
        self.replay_buffer = None
        self.optimizer = None
        self.default_lr = default_lr

        # Checkpoint and helper classes settings
        self.max_to_keep = max_to_keep
        if checkpoint_path is not None:
            self.checkpoint = tf.train.Checkpoint(model=self.amortizer)
            self.manager = tf.train.CheckpointManager(self.checkpoint, checkpoint_path, max_to_keep=max_to_keep)
            self.checkpoint.restore(self.manager.latest_checkpoint)
            self.loss_history.load_from_file(checkpoint_path)
            if self.simulation_memory is not None:
                self.simulation_memory.load_from_file(checkpoint_path)
            if self.manager.latest_checkpoint:
                logger.info("Networks loaded from {}".format(self.manager.latest_checkpoint))
            else:
                logger.info("Initialized networks from scratch.")
        else:
            self.checkpoint = None
            self.manager = None
        self.checkpoint_path = checkpoint_path

        # Perform a sanity check with provided components
        if not skip_checks:
            self._check_consistency()

    def diagnose_latent2d(self, inputs=None, **kwargs):
        """Performs visual pre-inference diagnostics of latent space on either provided validation data
        (new simulations) or internal simulation memory.
        If ``inputs is not None``, then diagnostics will be performed on the inputs, regardless
        whether the `simulation_memory` of the trainer is empty or not. If ``inputs is None``, then
        the trainer will try to access is memory or raise a `ConfigurationError`.

        Parameters
        ----------
        inputs   : None, list, or dict, optional, default: None
            The optional inputs to use

        Other Parameters
        ----------------

        conf_args :
           optional keyword arguments passed to the configurator
        net_args :
           optional keyword arguments passed to the amortizer
        plot_args :
           optional keyword arguments passed to `plot_latent_space_2d`

        Returns
        -------
        fig      : plt.Figure
            The figure object which can be readily saved to disk using `fig.savefig()`.
        """

        if type(self.amortizer) is AmortizedPosterior:
            # If no inputs, try memory and throw if no memory
            if inputs is None:
                if self.simulation_memory is None:
                    raise ConfigurationError(
                        "You should either enable simulation memory or supply the inputs argument."
                    )
                else:
                    inputs = self.simulation_memory.get_memory()
            else:
                inputs = self.configurator(inputs, **kwargs.pop("conf_args", {}))

            # Do inference
            if type(inputs) is list:
                z, _ = self.amortizer.call_loop(inputs, **kwargs.pop("net_args", {}))
            else:
                z, _ = self.amortizer(inputs, **kwargs.pop("net_args", {}))
            return plot_latent_space_2d(z, **kwargs.pop("plot_args", {}))
        else:
            raise NotImplementedError("Latent space diagnostics are only available for type AmortizedPosterior!")

    def diagnose_sbc_histograms(self, inputs=None, n_samples=None, **kwargs):
        """Performs visual pre-inference diagnostics via simulation-based calibration (SBC)
        (new simulations) or internal simulation memory.
        If ``inputs is not None``, then diagnostics will be performed on the inputs, regardless
        whether the `simulation_memory` of the trainer is empty or not. If ``inputs is None``, then
        the trainer will try to access is memory or raise a `ConfigurationError`.

        Parameters
        ----------
        inputs    : None, list or dict, optional, default: None
            The optional inputs to use
        n_samples : int or None, optional, default: None
            The number of posterior samples to draw for each simulated data set.
            If None, the number will be heuristically determined so that n_sim / n_draws is approximately equal to 20

        Other Parameters
        ----------------
        conf_args :
           optional keyword arguments passed to the configurator
        net_args :
           optional keyword arguments passed to the amortizer
        plot_args :
           optional keyword arguments passed to `plot_sbc()`

        Returns
        -------
        fig       : plt.Figure
            The figure object which can be readily saved to disk using `fig.savefig()`.
        """

        if type(self.amortizer) is AmortizedPosterior:
            # If no inputs, try memory and throw if no memory
            if inputs is None:
                if self.simulation_memory is None:
                    raise ConfigurationError("You should either ")
                else:
                    inputs = self.simulation_memory.get_memory()
            else:
                inputs = self.configurator(inputs, **kwargs.pop("conf_args", {}))

            # Heuristically determine the number of posterior samples
            if n_samples is None:
                if type(inputs) is list:
                    n_sim = np.sum([inp["parameters"].shape[0] for inp in inputs])
                    n_samples = int(np.ceil(n_sim / 20))
                else:
                    n_samples = int(np.ceil(inputs["parameters"].shape[0] / 20))

            # Do inference
            if type(inputs) is list:
                post_samples = self.amortizer.sample_loop(inputs, n_samples=n_samples, **kwargs.pop("net_args", {}))
                prior_samples = np.concatenate([inp["parameters"] for inp in inputs], axis=0)
            else:
                post_samples = self.amortizer(inputs, n_samples, n_samples, **kwargs.pop("net_args", {}))
                prior_samples = inputs["parameters"]

            # Check for prior names and override keyword if available
            plot_kwargs = kwargs.pop("plot_args", {})
            if type(self.generative_model) is GenerativeModel and plot_kwargs.get("param_names") is None:
                plot_kwargs["param_names"] = self.generative_model.param_names

            return plot_sbc_histograms(post_samples, prior_samples, **plot_kwargs)
        else:
            raise NotImplementedError("SBC diagnostics are only available for type AmortizedPosterior!")

    def load_pretrained_network(self):
        """Attempts to load a pre-trained network if checkpoint path is provided and a checkpoint manager exists."""

        if self.manager is None or self.checkpoint is None:
            return False
        status = self.checkpoint.restore(self.manager.latest_checkpoint)
        return status

    def train_online(
        self,
        epochs,
        iterations_per_epoch,
        batch_size,
        save_checkpoint=True,
        optimizer=None,
        reuse_optimizer=False,
        early_stopping=False,
        use_autograph=True,
        validation_sims=None,
        **kwargs,
    ):
        """Trains an amortizer via online learning. Additional keyword arguments
        are passed to the generative mode, configurator, and amortizer.

        Parameters
        ----------
        epochs               : int
            Number of epochs (and number of times a checkpoint is stored)
        iterations_per_epoch : int
            Number of batch simulations to perform per epoch
        batch_size           : int
            Number of simulations to perform at each backprop step
        save_checkpoint      : bool, default: True
            A flag to decide whether to save checkpoints after each epoch,
            if a checkpoint_path provided during initialization, otherwise ignored.
        optimizer            : tf.keras.optimizer.Optimizer or None
            Optimizer for the neural network. ``None`` will result in ``tf.keras.optimizers.Adam``
            using a learning rate of 5e-4 and a cosine decay from 5e-4 to 0. A custom optimizer
            will override default learning rate and schedule settings.
        reuse_optimizer      : bool, optional, default: False
            A flag indicating whether the optimizer instance should be treated as persistent or not.
            If ``False``, the optimizer and its states are not stored after training has finished.
            Otherwise, the optimizer will be stored as ``self.optimizer` and re-used in further training runs.
        early_stopping       : bool, optional, default: False
            Whether to use optional stopping or not during training. Could speed up training.
            Only works if ``validation_sims is not None``, i.e., validation data has been provided.
        use_autograph        : bool, optional, default: True
            Whether to use autograph for the backprop step. Could lead to enormous speed-ups but
            could also be harder to debug.
        validation_sims      : dict or None, optional, default: None
            Simulations used as a "validation set".
            If ``dict``, will assume it's the output of a generative model and try
            ``amortizer.compute_loss(configurator(validation_sims))``
            after each epoch.
            If ``int``, will assume it's the number of sims to generate from the generative
            model before starting training. Only considered if a generative model has been
            provided during initialization.
            If ``None`` (default), no validation set will be used.

        Other Parameters
        ----------------
        model_args :
           optional kwargs passed to the generative model
        val_model_args:
           optional kwargs passed to the generative model for generating validation data. Only useful if
           ``type(validation_sims) is int``.
        conf_args :
           optional kwargs passed to the configurator before each backprop (update) step.
        val_conf_args :
           optional kwargs passed to the configurator then configuring the validation data.
        net_args :
           optional kwargs passed to the amortizer
        early_stopping_args :
           optional kwargs passed to the `EarlyStopper`

        Returns
        -------
        losses : dict or pandas.DataFrame
            A dictionary storing the losses across epochs and iterations
        """

        assert self.generative_model is not None, "No generative model found. Only offline training is possible!"

        # Compile update function, if specified
        if use_autograph:
            _backprop_step = tf.function(backprop_step, reduce_retracing=True)
        else:
            _backprop_step = backprop_step

        # Create new optimizer and initialize loss history
        self._setup_optimizer(optimizer, epochs, iterations_per_epoch)
        self.loss_history.start_new_run()
        validation_sims = self._config_validation(validation_sims, **kwargs.pop("val_model_args", {}))

        # Create early stopper, if conditions met, otherwise None returned
        early_stopper = self._config_early_stopping(early_stopping, validation_sims, **kwargs)

        # Loop through training epochs
        for ep in range(1, epochs + 1):
            with tqdm(total=iterations_per_epoch, desc=f"Training epoch {ep}", mininterval=TQDM_MININTERVAL) as p_bar:
                for it in range(1, iterations_per_epoch + 1):
                    # Perform one training step and obtain current loss value
                    loss = self._train_step(batch_size, update_step=_backprop_step, **kwargs)

                    # Store returned loss
                    self.loss_history.add_entry(ep, loss)

                    # Compute running loss
                    avg_dict = self.loss_history.get_running_losses(ep)

                    # Extract current learning rate
                    lr = extract_current_lr(self.optimizer)

                    # Format for display on progress bar
                    disp_str = format_loss_string(ep, it, loss, avg_dict, lr=lr)

                    # Update progress bar
                    p_bar.set_postfix_str(disp_str, refresh=False)
                    p_bar.update(1)

            # Store and compute validation loss, if specified
            self._validation(ep, validation_sims, **kwargs)
            self._save_trainer(save_checkpoint)

            # Check early stopping, if specified
            if self._check_early_stopping(early_stopper):
                break

        # Remove optimizer reference, if not set as persistent
        if not reuse_optimizer:
            self.optimizer = None
        return self.loss_history.get_plottable()

    def train_offline(
        self,
        simulations_dict,
        epochs,
        batch_size,
        save_checkpoint=True,
        optimizer=None,
        reuse_optimizer=False,
        early_stopping=False,
        validation_sims=None,
        use_autograph=True,
        **kwargs,
    ):
        """Trains an amortizer via offline learning. Assume parameters, data and optional
        context have already been simulated (i.e., forward inference has been performed).

        Parameters
        ----------
        simulations_dict : dict
           A dictionary containing the simulated data / context, if using the default keys,
           the method expects at least the mandatory keys ``sim_data`` and ``prior_draws`` to be present
        epochs           : int
           Number of epochs (and number of times a checkpoint is stored)
        batch_size       : int
           Number of simulations to perform at each backpropagation step
        save_checkpoint  : bool, default: True
           Determines whether to save checkpoints after each epoch,
           if a checkpoint_path provided during initialization, otherwise ignored.
        optimizer         : tf.keras.optimizer.Optimizer or None
           Optimizer for the neural network. ``None`` will result in ``tf.keras.optimizers.Adam``
           using a learning rate of 5e-4 and a cosine decay from 5e-4 to 0. A custom optimizer
           will override default learning rate and schedule settings.
        reuse_optimizer   : bool, optional, default: False
           A flag indicating whether the optimizer instance should be treated as persistent or not.
           If ``False``, the optimizer and its states are not stored after training has finished.
           Otherwise, the optimizer will be stored as ``self.optimizer`` and re-used in further training runs.
        early_stopping    : bool, optional, default: False
           Whether to use optional stopping or not during training. Could speed up training.
           Only works if ``validation_sims is not None``, i.e., validation data has been provided.
        use_autograph     : bool, optional, default: True
           Whether to use autograph for the backprop step. Could lead to enormous speed-ups but
           could also be harder to debug.
        validation_sims      : dict, int, or None, optional, default: None
           Simulations used as a "validation set".
           If ``dict``, will assume it's the output of a generative model and try
           ``amortizer.compute_loss(configurator(validation_sims))`` after each epoch.
           If ``int``, will assume it's the number of sims to generate from the generative
           model before starting training. Only considered if a generative model has been
           provided during initialization.
           If ``None`` (default), no validation set will be used.

        Other Parameters
        ----------------
        val_model_args :
           optional kwargs passed to the generative model for generating validation data.
           Only useful if ``type(validation_sims) is int``.
        conf_args :
           optional kwargs passed to the configurator before each backprop (update) step.
        val_conf_args :
           optional kwargs passed to the configurator then configuring the validation data.
        net_args :
           optional kwargs passed to the amortizer
        early_stopping_args :
           optional kwargs passed to the `EarlyStopper`

        Returns
        -------
        losses : ``dict`` or ``pandas.DataFrame``
           A dictionary or a data frame storing the losses across epochs and iterations

        """

        # Compile update function, if specified
        if use_autograph:
            _backprop_step = tf.function(backprop_step, reduce_retracing=True)
        else:
            _backprop_step = backprop_step

        # Inits
        if isinstance(self.amortizer, AmortizedModelComparison):
            data_set = MultiSimulationDataset(simulations_dict, batch_size)
        else:
            data_set = SimulationDataset(simulations_dict, batch_size)
        self._setup_optimizer(optimizer, epochs, data_set.num_batches)
        self.loss_history.start_new_run()
        validation_sims = self._config_validation(validation_sims, **kwargs.pop("val_model_args", {}))

        # Create early stopper, if conditions met, otherwise None returned
        early_stopper = self._config_early_stopping(early_stopping, validation_sims, **kwargs)

        # Loop through epochs
        for ep in range(1, epochs + 1):
            with tqdm(
                total=data_set.num_batches, desc="Training epoch {}".format(ep), mininterval=TQDM_MININTERVAL
            ) as p_bar:
                # Loop through dataset
                for bi, forward_dict in enumerate(data_set, start=1):
                    # Perform one training step and obtain current loss value
                    input_dict = self.configurator(forward_dict, **kwargs.pop("conf_args", {}))
                    loss = self._train_step(batch_size, _backprop_step, input_dict, **kwargs)

                    # Store returned loss
                    self.loss_history.add_entry(ep, loss)

                    # Compute running loss
                    avg_dict = self.loss_history.get_running_losses(ep)

                    # Extract current learning rate
                    lr = extract_current_lr(self.optimizer)

                    # Format for display on progress bar
                    disp_str = format_loss_string(ep, bi, loss, avg_dict, lr=lr, it_str="Batch")

                    # Update progress bar
                    p_bar.set_postfix_str(disp_str, refresh=False)
                    p_bar.update(1)

            # Store and compute validation loss, if specified
            self._validation(ep, validation_sims, **kwargs)
            self._save_trainer(save_checkpoint)

            # Check early stopping, if specified
            if self._check_early_stopping(early_stopper):
                break

        # Remove optimizer reference, if not set as persistent
        if not reuse_optimizer:
            self.optimizer = None
        return self.loss_history.get_plottable()

    def train_from_presimulation(
        self,
        presimulation_path,
        optimizer,
        save_checkpoint=True,
        max_epochs=None,
        reuse_optimizer=False,
        custom_loader=None,
        early_stopping=False,
        validation_sims=None,
        use_autograph=True,
        **kwargs,
    ):
        """Trains an amortizer via a modified form of offline training.

        Like regular offline training, it assumes that parameters, data and optional context have already
        been simulated (i.e., forward inference has been performed).

        Also like regular offline training, it is faster than online training in scenarios where simulations are slow.
        Unlike regular offline training, it uses each batch from the presimulated dataset only once during training,
        if not otherwise specified by a higher maximal number of epochs. Then, presimulated data is reused in a cyclic
        manner to achieve the desired number of epochs.
        A larger presimulated dataset is therefore required than for offline training, and the increase in speed
        gained by loading simulations instead of generating them on the fly comes at a cost:
        a large presimulated dataset takes up a large amount of hard drive space.

        Parameters
        ----------
        presimulation_path   : str
            File path to the folder containing the files from the precomputed simulation.
            Ideally generated using a GenerativeModel's presimulate_and_save method, otherwise must match
            the structure produced by that method.
            Each file contains the data for one epoch (i.e. a number of batches), and must be compatible
            with the custom_loader provided.
            The custom_loader must read each file into a collection (either a dictionary or a list) of simulation_dict
            objects.
            This is easily achieved with the pickle library: if the files were generated from collections of
            simulation_dict objects using pickle.dump, the _default_loader (default for custom_load) will
            load them using pickle.load.
            Training parameters like number of iterations and batch size are inferred from the files during training.
        optimizer            : tf.keras.optimizer.Optimizer
            Optimizer for the neural network training. Since for this training, it is impossible to guess the number of
            iterations beforehead, an optimizer must be provided.
        save_checkpoint      : bool, optional, default : True
            Determines whether to save checkpoints after each epoch,
            if a checkpoint_path provided during initialization, otherwise ignored.
        max_epochs           : int or None, optional, default: None
            An optional parameter to limit or extend the number of epochs. If number of epochs is larger than the files
            of the dataset, presimulations will be reused.
        reuse_optimizer      : bool, optional, default: False
            A flag indicating whether the optimizer instance should be treated as persistent or not.
            If ``False``, the optimizer and its states are not stored after training has finished.
            Otherwise, the optimizer will be stored as ``self.optimizer`` and re-used in further training runs.
        custom_loader        : callable, optional, default: self._default_loader
            Must take a string file_path as an input and output a collection (dictionary or list) of
            simulation_dict objects. A simulation_dict has the keys ``prior_non_batchable_context``,
            ``prior_batchable_context``, ``prior_draws``, ``sim_non_batchable_context``, ``sim_batchable_context``, and
            ``sim_data``.
            Here, ``prior_draws`` and ``sim_data`` must have actual data as values, the rest are optional.
        early_stopping       : bool, optional, default: False
            Whether to use optional stopping or not during training. Could speed up training.
        validation_sims      : dict, int, or None, optional, default: None
            Simulations used as a validation set.
            If ``dict``, will assume it's the output of a generative model and try
            ``amortizer.compute_loss(configurator(validation_sims))``
            after each epoch.
            If ``int``, will assume it's the number of sims to generate from the generative
            model before starting training. Only considered if a generative model has been
            provided during initialization.
            If ``None`` (default), no validation set will be used.
        use_autograph        : bool, optional, default: True
            Whether to use autograph for the backprop step. Could lead to enormous speed-ups but
            could also be harder to debug.

        Other Parameters
        ----------------

        conf_args :
           optional keyword arguments passed to the configurator
        net_args :
           optional keyword arguments passed to the amortizer

        Returns
        -------
        losses : ``dict`` or ``pandas.DataFrame``
            A dictionary or a data frame storing the losses across epochs and iterations
        """

        self.optimizer = optimizer

        # Compile update function, if specified
        if use_autograph:
            _backprop_step = tf.function(backprop_step, reduce_retracing=True)
        else:
            _backprop_step = backprop_step

        # Inits
        self.loss_history.start_new_run()
        validation_sims = self._config_validation(validation_sims, **kwargs.pop("val_model_args", {}))

        # Create early stopper, if conditions met, otherwise None returned
        early_stopper = self._config_early_stopping(early_stopping, validation_sims, **kwargs)

        # Loop over the presimulated dataset.
        file_list = os.listdir(presimulation_path)

        # Use default loading function if none is provided
        if custom_loader is None:
            custom_loader = self._default_loader
            # Remove non-pickle files from the list
            file_list = [f for f in file_list if f.endswith(".pkl")]

        if max_epochs is not None:
            # Limit number of epochs to max_epochs
            if len(file_list) > max_epochs:
                file_list = file_list[:max_epochs]
            # If the number of files is smaller than the number of epochs, repeat the files until max_epochs is reached
            elif len(file_list) < max_epochs:
                file_list = file_list * int(np.ceil(max_epochs / len(file_list)))
                file_list = file_list[:max_epochs]

        for ep, current_filename in enumerate(file_list, start=1):
            # Read single file into memory as a dictionary or list
            file_path = os.path.join(presimulation_path, current_filename)
            epoch_data = custom_loader(file_path)

            # For each epoch, the number of iterations is inferred from the presimulated dictionary or
            # list used for that epoch
            if isinstance(epoch_data, dict):
                index_list = list(epoch_data.keys())
            elif isinstance(epoch_data, list):
                index_list = np.arange(len(epoch_data))
            else:
                raise ValueError(
                    f"Loading a simulation file resulted in a {type(epoch_data)}. Must be a dictionary or a list!"
                )

            with tqdm(total=len(index_list), desc=f"Training epoch {ep}", mininterval=TQDM_MININTERVAL) as p_bar:
                for it, index in enumerate(index_list, start=1):
                    # Perform one training step and obtain current loss value
                    input_dict = self.configurator(epoch_data[index])

                    # Like the number of iterations, the batch size is inferred from presimulated dictionary or list
                    if isinstance(self.amortizer, AmortizedModelComparison):
                        batch_size = input_dict[DEFAULT_KEYS["summary_conditions"]].shape[0]
                    else:
                        batch_size = epoch_data[index][DEFAULT_KEYS["sim_data"]].shape[0]
                    loss = self._train_step(batch_size, _backprop_step, input_dict, **kwargs)

                    # Store returned loss
                    self.loss_history.add_entry(ep, loss)

                    # Compute running loss
                    avg_dict = self.loss_history.get_running_losses(ep)

                    # Extract current learning rate
                    lr = extract_current_lr(self.optimizer)

                    # Format for display on progress bar
                    disp_str = format_loss_string(ep, it, loss, avg_dict, lr=lr)

                    # Update progress bar
                    p_bar.set_postfix_str(disp_str, refresh=False)
                    p_bar.update(1)

            # Store after each epoch, if specified
            self._validation(ep, validation_sims, **kwargs)
            self._save_trainer(save_checkpoint)

            # Check early stopping, if specified
            if self._check_early_stopping(early_stopper):
                break

        # Remove optimizer reference, if not set as persistent
        if not reuse_optimizer:
            self.optimizer = None
        return self.loss_history.get_plottable()

    def train_experience_replay(
        self,
        epochs,
        iterations_per_epoch,
        batch_size,
        save_checkpoint=True,
        optimizer=None,
        reuse_optimizer=False,
        buffer_capacity=1000,
        early_stopping=False,
        use_autograph=True,
        validation_sims=None,
        **kwargs,
    ):
        """Trains the network(s) via experience replay using a memory replay buffer, as utilized
        in reinforcement learning. Additional keyword arguments are passed to the generative mode,
        configurator, and amortizer. Read below for signature.

        Parameters
        ----------
        epochs               : int
            Number of epochs (and number of times a checkpoint is stored)
        iterations_per_epoch : int
            Number of batch simulations to perform per epoch
        batch_size           : int
            Number of simulations to perform at each backpropagation step.
        save_checkpoint      : bool, optional, default: True
            A flag to decide whether to save checkpoints after each epoch,
            if a ``checkpoint_path`` provided during initialization, otherwise ignored.
        optimizer            : tf.keras.optimizer.Optimizer or None
            Optimizer for the neural network. ``None`` will result in ``tf.keras.optimizers.Adam``
            using a learning rate of 5e-4 and a cosine decay from 5e-4 to 0. A custom optimizer
            will override default learning rate and schedule settings.
        reuse_optimizer      : bool, optional, default: False
            A flag indicating whether the optimizer instance should be treated as persistent or not.
            If ``False``, the optimizer and its states are not stored after training has finished.
            Otherwise, the optimizer will be stored as ``self.optimizer`` and re-used in further training runs.
        buffer_capacity      : int, optional, default: 1000
            Max number of batches to store in buffer. For instance, if ``batch_size=32``
            and ``capacity_in_batches=1000``, then the buffer will hold a maximum of
            32 * 1000 = 32000 simulations. Be careful with memory!
            Important! Argument will be ignored if buffer has previously been initialized!
        early_stopping       : bool, optional, default: True
            Whether to use optional stopping or not during training. Could speed up training.
            Only works if ``validation_sims is not None``, i.e., validation data has been provided.
        use_autograph        : bool, optional, default: True
            Whether to use autograph for the backprop step. Could lead to enormous speed-ups but
            could also be harder to debug.
        validation_sims      : dict or None, optional, default: None
            Simulations used as a "validation set".
            If ``dict``, will assume it's the output of a generative model and try
            ``amortizer.compute_loss(configurator(validation_sims))``
            after each epoch.
            If ``int``, will assume it's the number of sims to generate from the generative
            model before starting training. Only considered if a generative model has been
            provided during initialization.
            If ``None`` (default), no validation set will be used.

        Other Parameters
        ----------------
        model_args :
           optional kwargs passed to the generative model
        val_model_args :
           optional kwargs passed to the generative model for generating validation data. Only useful if
           ``type(validation_sims) is int``.
        conf_args :
           optional kwargs passed to the configurator before each backprop (update) step.
        val_conf_args :
           optional kwargs passed to the configurator then configuring the validation data.
        net_args :
           optional kwargs passed to the amortizer
        early_stopping_args:
           optional kwargs passed to the `EarlyStopper`

        Returns
        -------
        losses : ``dict`` or ``pandas.DataFrame``
            A dictionary or a data frame storing the losses across epochs and iterations.
        """

        assert self.generative_model is not None, "No generative model found. Only offline training is possible!"

        # Compile update function, if specified
        if use_autograph:
            _backprop_step = tf.function(backprop_step, reduce_retracing=True)
        else:
            _backprop_step = backprop_step

        # Inits
        self._setup_optimizer(optimizer, epochs, iterations_per_epoch)
        self.loss_history.start_new_run()
        if self.replay_buffer is None:
            self.replay_buffer = MemoryReplayBuffer(buffer_capacity)
        validation_sims = self._config_validation(validation_sims)

        # Create early stopper, if conditions met, otherwise None returned
        early_stopper = self._config_early_stopping(early_stopping, validation_sims, **kwargs)

        # Loop through epochs
        for ep in range(1, epochs + 1):
            with tqdm(total=iterations_per_epoch, desc=f"Training epoch {ep}", mininterval=TQDM_MININTERVAL) as p_bar:
                for it in range(1, iterations_per_epoch + 1):
                    # Simulate a batch of data and store into buffer
                    input_dict = self._forward_inference(
                        batch_size, **kwargs.pop("conf_args", {}), **kwargs.pop("model_args", {})
                    )
                    self.replay_buffer.store(input_dict)

                    # Sample from buffer
                    input_dict = self.replay_buffer.sample()

                    # One step backprop
                    loss = _backprop_step(input_dict, self.amortizer, self.optimizer, **kwargs.pop("net_args", {}))

                    # Store returned loss
                    self.loss_history.add_entry(ep, loss)

                    # Compute running loss
                    avg_dict = self.loss_history.get_running_losses(ep)

                    # Extract current learning rate
                    lr = extract_current_lr(self.optimizer)

                    # Format for display on progress bar
                    disp_str = format_loss_string(ep, it, loss, avg_dict, lr=lr)

                    # Update progress bar
                    p_bar.set_postfix_str(disp_str, refresh=False)
                    p_bar.update(1)

            # Store and compute validation loss, if specified
            self._validation(ep, validation_sims, **kwargs)
            self._save_trainer(save_checkpoint)

            # Check early stopping, if specified
            if self._check_early_stopping(early_stopper):
                break

        # Remove optimizer reference, if not set as persistent
        if not reuse_optimizer:
            self.optimizer = None
        return self.loss_history.get_plottable()

    def train_rounds(
        self,
        rounds,
        sim_per_round,
        epochs,
        batch_size,
        save_checkpoint=True,
        optimizer=None,
        reuse_optimizer=False,
        early_stopping=False,
        use_autograph=True,
        validation_sims=None,
        **kwargs,
    ):
        """Trains an amortizer via round-based learning. In each round, ``sim_per_round`` data sets
        are simulated from the generative model and added to the data sets simulated in previous
        round. Then, the networks are trained for ``epochs`` on the augmented set of data sets.

        .. note::
           Training time will increase from round to round, since the number of simulations
           increases correspondingly. The final round will then train the networks on ``rounds * sim_per_round``
           data sets, so make sure this number does not eat up all available memory.

        Parameters
        ----------
        rounds               : int
            Number of rounds to perform (outer loop)
        sim_per_round        : int
            Number of simulations per round
        epochs               : int
            Number of epochs (and number of times a checkpoint is stored, inner loop) within a round.
        batch_size           : int
            Number of simulations to use at each backpropagation step
        save_checkpoint : bool, optional, default: True
            A flag to decide whether to save checkpoints after each epoch,
            if a checkpoint_path provided during initialization, otherwise ignored.
        optimizer            : tf.keras.optimizer.Optimizer or None
            Optimizer for the neural network training. ``None`` will result in ``tf.keras.optimizers.Adam``
            using a learning rate of 5e-4 and a cosine decay from 5e-4 to 0. A custom optimizer
            will override default learning rate and schedule settings.
        reuse_optimizer      : bool, optional, default: False
            A flag indicating whether the optimizer instance should be treated as persistent or not.
            If ``False``, the optimizer and its states are not stored after training has finished.
            Otherwise, the optimizer will be stored as ``self.optimizer`` and re-used in further training runs.
        early_stopping       : bool, optional, default: False
            Whether to use optional stopping or not during training. Could speed up training.
            Only works if ``validation_sims is not None``, i.e., validation data has been provided.
            Will be performed within rounds, not between rounds!
        use_autograph        : bool, optional, default: True
            Whether to use autograph for the backprop step. Could lead to enormous speed-ups but
            could also be harder to debug.
        validation_sims      : dict or None, optional, default: None
            Simulations used as a "validation set".
            If ``dict``, will assume it's the output of a generative model and try
            ``amortizer.compute_loss(configurator(validation_sims))``
            after each epoch.
            If ``int``, will assume it's the number of sims to generate from the generative
            model before starting training. Only considered if a generative model has been
            provided during initialization.
            If ``None`` (default), no validation set will be used.

        Other Parameters
        ----------------

        model_args :
           optional kwargs passed to the generative model
        val_model_args :
           optional kwargs passed to the generative model for generating validation data. Only useful if
           ``type(validation_sims) is int``.
        conf_args :
           optional kwargs passed to the configurator before each backprop (update) step.
        val_conf_args :
           optional kwargs passed to the configurator then configuring the validation data.
        net_args :
           optional kwargs passed to the amortizer
        early_stopping_args :
           optional kwargs passed to the `EarlyStopper`

        Returns
        -------
        losses : ``dict`` or ``pandas.DataFrame``
            A dictionary or a data frame storing the losses across epochs and iterations
        """

        assert self.generative_model is not None, "No generative model found. Only offline training is possible!"

        # Prepare logger
        logger = logging.getLogger()

        # Create new optimizer and initialize loss history, needs to calculate iters per epoch
        batches_per_sim = np.ceil(sim_per_round / batch_size)
        sum_total = (rounds + rounds**2) / 2
        iterations_per_epoch = int(batches_per_sim * sum_total)
        self._setup_optimizer(optimizer, epochs, iterations_per_epoch)
        validation_sims = self._config_validation(validation_sims)

        # Loop for each round
        first_round = True
        for r in range(1, rounds + 1):
            # Data generation step
            if first_round:
                # Simulate initial data
                logger.info(f"Simulating initial {sim_per_round} data sets for training...")
                simulations_dict = self._forward_inference(sim_per_round, configure=False, **kwargs)
                first_round = False
            else:
                # Simulate further data
                logger.info(f"Simulating new {sim_per_round} data sets and appending to previous...")
                logger.info(f"New total number of simulated data sets for training: {sim_per_round * r}")
                simulations_dict_r = self._forward_inference(sim_per_round, configure=False, **kwargs)

                # Attempt to concatenate data sets
                for k in simulations_dict.keys():
                    if simulations_dict[k] is not None:
                        simulations_dict[k] = np.concatenate((simulations_dict[k], simulations_dict_r[k]), axis=0)

            # Train offline with generated stuff
            _ = self.train_offline(
                simulations_dict,
                epochs,
                batch_size,
                save_checkpoint,
                reuse_optimizer=True,
                early_stopping=early_stopping,
                use_autograph=use_autograph,
                validation_sims=validation_sims,
                **kwargs,
            )

        # Remove optimizer reference, if not set as persistent
        if not reuse_optimizer:
            self.optimizer = None
        return self.loss_history.get_plottable()

    def mmd_hypothesis_test(
        self, observed_data, reference_data=None, num_reference_simulations=1000, num_null_samples=100, bootstrap=False
    ):
        """Performs a sampling-based hypothesis test for detecting Out-Of-Simulation (model misspecification).

        Parameters
        ----------
        observed_data : np.ndarray
           Observed data, shape (num_observed, ...)
        reference_data : np.ndarray
           Reference data representing samples from the well-specified model, shape (num_reference, ...)
        num_reference_simulations : int, default: 1000
           Number of reference simulations (M) simulated from the trainer's generative model
           if no `reference_data` are provided.
        num_null_samples : int, default: 100
           Number of draws from the MMD sampling distribution under the null hypothesis "the trainer's generative
           model is well-specified"
        bootstrap : bool, default: False
           If true, the reference data (see above) are bootstrapped for each sample from the MMD sampling distribution.
           If false, a new data set is simulated for computing each draw from the MMD sampling distribution.

        Returns
        -------
        mmd_null_samples : np.ndarray
           samples from the H0 sampling distribution ("well-specified model")
        mmd_observed : float
           summary MMD estimate for the observed data sets
        """

        if reference_data is None:
            if self.generative_model is None:
                raise ArgumentError("If you do not provide reference data, your trainer must have a generative model!")

            reference_data = self.configurator(self.generative_model(num_reference_simulations))

        if type(reference_data) == dict and "summary_conditions" in reference_data.keys():
            reference_summary = self.amortizer.summary_net(reference_data["summary_conditions"])
        else:
            reference_summary = self.amortizer.summary_net(reference_data)

        if type(observed_data) == dict and "summary_conditions" in observed_data.keys():
            observed_summary = self.amortizer.summary_net(observed_data["summary_conditions"])
        else:
            observed_summary = self.amortizer.summary_net(observed_data)

        num_observed = observed_summary.shape[0]
        num_reference = reference_summary.shape[0]

        mmd_null_samples = np.empty(num_null_samples, dtype=np.float32)
        for i in tqdm(range(num_null_samples), mininterval=TQDM_MININTERVAL):
            if bootstrap:
                bootstrap_idx = np.random.randint(0, num_reference, size=num_observed)
                simulated_summary = tf.gather(reference_summary, bootstrap_idx, axis=0)
            else:
                simulated_data = self.configurator(self.generative_model(num_observed))
                simulated_summary = self.amortizer.summary_net(simulated_data["summary_conditions"])

            mmd_null_samples[i] = np.sqrt(maximum_mean_discrepancy(reference_summary, simulated_summary).numpy())

        mmd_observed = np.sqrt(maximum_mean_discrepancy(reference_summary, observed_summary).numpy())

        return mmd_null_samples, mmd_observed

    def _config_validation(self, validation_sims, **kwargs):
        """Helper method to prepare validation set based on user input."""

        logger = logging.getLogger()
        if validation_sims is None:
            return None
        if type(validation_sims) is dict:
            return validation_sims
        if type(validation_sims) is int:
            if self.generative_model is not None:
                vals = self.generative_model(validation_sims, **kwargs)
                logger.info(f"Generated {validation_sims} simulations for validation.")
                return vals
            else:
                logger.warning(
                    "Validation simulations can only be generated if the Trainer is initialized "
                    + "with a generative model."
                )
                return None
        logger.warning('Type of argument "validation_sims" not understood. No validation simulations were created.')

    def _config_early_stopping(self, early_stopping, validation_sims, **kwargs):
        """Helper method to configure early stopping or warn user for."""

        if early_stopping:
            if validation_sims is not None:
                early_stopper = EarlyStopper(**kwargs.pop("early_stopping_args", {}))
            else:
                logger = logging.getLogger()
                logger.warning("No early stopping will be used, since validation_sims were not provided.")
                early_stopper = None
            return early_stopper
        return None

    def _setup_optimizer(self, optimizer, epochs, iterations_per_epoch):
        """Helper method to prepare optimizer based on user input."""

        if optimizer is None:
            # No optimizer so far and None provided
            if self.optimizer is None:
                # Calculate decay steps for default cosine decay
                schedule = tf.keras.optimizers.schedules.CosineDecay(
                    self.default_lr, iterations_per_epoch * epochs, name="lr_decay"
                )
                self.optimizer = tf.keras.optimizers.Adam(schedule, **OPTIMIZER_DEFAULTS)
            # No optimizer provided, but optimizer exists, that is,
            # has been declared as persistent, so do nothing
            else:
                pass
        else:
            self.optimizer = optimizer

    def _save_trainer(self, save_checkpoint):
        """Helper method to take care of IO operations."""

        if self.manager is not None and save_checkpoint:
            self.manager.save()
            self.loss_history.save_to_file(file_path=self.checkpoint_path, max_to_keep=self.max_to_keep)
            if self.simulation_memory is not None:
                self.simulation_memory.save_to_file(file_path=self.checkpoint_path)

    def _validation(self, ep, validation_sims, **kwargs):
        """Helper method to take care of computing the validation loss(es)."""

        if validation_sims is not None:
            conf = self.configurator(validation_sims, **kwargs.pop("val_conf_args", {}))
            val_loss = self.amortizer.compute_loss(conf, **kwargs.pop("net_args", {}))
            self.loss_history.add_val_entry(ep, val_loss)
            val_loss_str = loss_to_string(ep, val_loss)
            logger = logging.getLogger()
            logger.info(val_loss_str)

    def _check_early_stopping(self, early_stopper):
        """Helper method to check improvement in validation loss."""

        if early_stopper is not None:
            if early_stopper.update_and_recommend(self.loss_history.last_total_val_loss()):
                logger = logging.getLogger()
                logger.info("Early stopping triggered.")
                return True
        return False

    def _train_step(self, batch_size, update_step, input_dict=None, **kwargs):
        """Performs forward inference -> configuration -> network -> loss pipeline.

        Parameters
        ----------
        batch_size    : int
            Number of simulations to perform at each backprop step
        update_step   : callable
            The function which will perform one backprop step on a batch. Should have the following signature:
            ``update_step(input_dict, amortizer, optimizer, **kwargs)``
        input_dict    : dict
            The optional pre-configured forward dict from a generative model, simulated, if None

        Other Parameters
        ----------------

        model_args :
           optional keyword arguments passed to the generative model
        conf_args :
           optional keyword arguments passed to the configurator
        net_args :
           optional keyword arguments passed to the amortizer

        """

        if input_dict is None:
            input_dict = self._forward_inference(
                batch_size, **kwargs.pop("conf_args", {}), **kwargs.pop("model_args", {})
            )
        if self.simulation_memory is not None:
            self.simulation_memory.store(input_dict)
        loss = update_step(input_dict, self.amortizer, self.optimizer, **kwargs.pop("net_args", {}))
        return loss

    def _forward_inference(self, n_sim, configure=True, **kwargs):
        """Performs one step of single-model forward inference.

        Parameters
        ----------
        n_sim         : int
            Number of simulations to perform at the given step (i.e., batch size)
        configure     : bool, optional, default: True
            Determines whether to pass the forward inputs through a configurator.
        **kwargs      : dict
            Optional keyword arguments passed to the generative model

        Returns
        -------
        out_dict : dict
            The outputs of the generative model.

        Raises
        ------
        SimulationError
            If the trainer has no generative model but ``trainer._forward_inference``
            is called (i.e., needs to simulate data from the generative model)
        """

        if self.generative_model is None:
            raise SimulationError("No generative model specified. Only offline learning is available!")
        out_dict = self.generative_model(n_sim, **kwargs.pop("model_args", {}))
        if configure:
            out_dict = self.configurator(out_dict, **kwargs.pop("conf_args", {}))
        return out_dict

    def _manage_configurator(self, config_fun, **kwargs):
        """Determines which configurator to use if None specified during construction."""

        # Do nothing if callable provided
        if callable(config_fun):
            return config_fun
        # If None of something else (default), infer default config based on amortizer type
        else:
            # Amortized posterior
            if isinstance(self.amortizer, AmortizedPosterior):
                default_config = DefaultPosteriorConfigurator()

            # Amortized lieklihood
            elif isinstance(self.amortizer, AmortizedLikelihood):
                default_config = DefaultLikelihoodConfigurator()

            # Joint amortizer
            elif isinstance(self.amortizer, AmortizedPosteriorLikelihood):
                default_config = DefaultJointConfigurator()

            # Model comparison amortizer
            elif isinstance(self.amortizer, AmortizedModelComparison):
                if kwargs.get("num_models") is None:
                    raise ConfigurationError(
                        'Either your generative model or amortizer should have "num_models" attribute, or '
                        + "you need initialize Trainer with num_models explicitly!"
                    )
                default_config = DefaultModelComparisonConfigurator(kwargs.get("num_models"))
            # Unknown raises an error
            else:
                raise NotImplementedError(
                    f"Could not initialize configurator based on " + f"amortizer type {type(self.amortizer)}!"
                )
            return default_config

    def _check_consistency(self):
        """Attempts to run one step generative_model -> configurator -> amortizer -> loss with
        batch_size=2. Should be skipped if generative model has non-standard behavior.

        Raises
        ------
        ConfigurationError
            If any operation along the above chain fails.
        """

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        if self.generative_model is not None:
            _n_sim = 2
            try:
                logger.info("Performing a consistency check with provided components...")
                _ = self.amortizer.compute_loss(self.configurator(self.generative_model(_n_sim)))
                logger.info("Done.")
            except Exception as err:
                raise ConfigurationError(
                    "Could not carry out computations of generative_model ->"
                    + f"configurator -> amortizer -> loss! Error trace:\n {err}"
                )

    def _default_loader(self, file_path):
        """Uses pickle to load as a default."""

        with open(file_path, "rb+") as f:
            loaded_file = pickle_load(f)
        return loaded_file
