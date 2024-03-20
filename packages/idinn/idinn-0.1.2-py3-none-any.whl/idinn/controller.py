import matplotlib.pyplot as plt
import numpy as np
import torch


class NeuralControllerMixIn():
    def save(self, checkpoint_path):
        torch.save(self.state_dict(), checkpoint_path)

    def load(self, checkpoint_path):
        self.load_state_dict(torch.load(checkpoint_path))


class SingleSourcingNeuralController(torch.nn.Module, NeuralControllerMixIn):
    """
    SingleSourcingNeuralController is a neural network-based controller for inventory optimization in a single-sourcing scenario.

    Parameters
    ----------
    hidden_layers : list
        List of integers representing the number of units in each hidden layer. Default is [2].
    activation : torch.nn.Module
        Activation function to be used in the hidden layers. Default is torch.nn.CELU(alpha=1).

    Attributes
    ----------
    hidden_layers : list
        List of integers representing the number of units in each hidden layer.
    activation : torch.nn.Module
        Activation function used in the hidden layers.
    stack : torch.nn.Sequential
        Sequential stack of linear layers and activation functions.

    Methods
    -------
    init_layers(lead_time)
        Initializes the layers of the neural network based on the lead time.
    forward(current_inventory, past_orders)
        Performs forward pass through the neural network.
    get_total_cost(sourcing_model, sourcing_periods, seed=None)
        Calculates the total cost over a given number of sourcing periods.
    train(sourcing_model, sourcing_periods, epochs, ...)
        Trains the neural network controller using the sourcing model and specified parameters.
    simulate(sourcing_model, sourcing_periods)
        Simulates the inventory and order quantities over a given number of sourcing periods.
    plot(sourcing_model, sourcing_periods)
        Plots the inventory and order quantities over a given number of sourcing periods.
    """

    def __init__(self, hidden_layers=[2], activation=torch.nn.CELU(alpha=1)):
        super().__init__()
        self.hidden_layers = hidden_layers
        self.activation = activation
        self.lead_time = None
        self.stack = None

    def init_layers(self, lead_time):
        """
        Initializes the layers of the neural network based on the lead time.

        Parameters
        ----------
        lead_time : int
            The lead time for sourcing.

        Returns
        -------
        None
        """
        self.lead_time = lead_time
        architecture = [
            torch.nn.Linear(lead_time + 1, self.hidden_layers[0]),
            self.activation,
        ]
        for i in range(len(self.hidden_layers)):
            if i < len(self.hidden_layers) - 1:
                architecture += [
                    torch.nn.Linear(self.hidden_layers[i], self.hidden_layers[i + 1]),
                    self.activation,
                ]
        architecture += [
            torch.nn.Linear(self.hidden_layers[-1], 1, bias=False),
            torch.nn.ReLU(),
        ]
        self.stack = torch.nn.Sequential(*architecture)

    def forward(
        self,
        current_inventory,
        past_orders,
    ):
        """
        Performs forward pass through the neural network.

        Parameters
        ----------
        current_inventory : torch.Tensor
            Current inventory levels.
        past_orders : torch.Tensor
            Past order quantities.

        Returns
        -------
        torch.Tensor
            Predicted order quantities.
        """
        if self.lead_time > 0:
            h = torch.cat([current_inventory, past_orders[:, -self.lead_time :]], dim=1)
        else:
            h = current_inventory
        h = self.stack(h)
        q = h - torch.frac(h).clone().detach()
        return q

    def get_total_cost(self, sourcing_model, sourcing_periods, seed=None):
        """
        Calculates the total cost over a given number of sourcing periods.

        Parameters
        ----------
        sourcing_model : SourcingModel
            The sourcing model to be used for cost calculation.
        sourcing_periods : int
            The number of sourcing periods.
        seed : int, optional
            Random seed for reproducibility. Default is None.

        Returns
        -------
        numpy.ndarray
            Total cost over the sourcing periods.
        """
        if seed is not None:
            torch.manual_seed(seed)

        if self.lead_time is None:
            self.init_layers(sourcing_model.get_lead_time())

        total_cost = 0
        for i in range(sourcing_periods):
            current_inventory = sourcing_model.get_current_inventory()
            past_orders = sourcing_model.get_past_orders()
            q = self.forward(current_inventory, past_orders)
            sourcing_model.order(q)
            current_cost = sourcing_model.get_cost()
            total_cost += current_cost.mean()
        return total_cost

    def train(
        self,
        sourcing_model,
        sourcing_periods,
        epochs,
        validation_sourcing_periods=None,
        lr_init_inventory=1e-1,
        lr_parameters=3e-3,
        seed=None,
        tensorboard_writer=None,
    ):
        """
        Trains the neural network controller using the sourcing model and specified parameters.

        Parameters
        ----------
        sourcing_model : SourcingModel
            The sourcing model to be used for training.
        sourcing_periods : int
            The number of sourcing periods for training.
        epochs : int
            The number of training epochs.
        validation_sourcing_periods : int, optional
            The number of sourcing periods for validation. Default is None.
        lr_init_inventory : float, optional
            Learning rate for initializing inventory. Default is 1e-1.
        lr_parameters : float, optional
            Learning rate for updating neural network parameters. Default is 3e-3.
        seed : int, optional
            Random seed for reproducibility. Default is None.
        tensorboard_writer : tensorboard.SummaryWriter, optional
            Tensorboard writer for logging. Default is None.

        Returns
        -------
        None
        """
        if seed is not None:
            torch.manual_seed(seed)

        optimizer_init_inventory = torch.optim.RMSprop(
            [sourcing_model.init_inventory], lr=lr_init_inventory
        )
        optimizer_parameters = torch.optim.RMSprop(self.parameters(), lr=lr_parameters)
        min_cost = np.inf

        for epoch in range(epochs):
            # Clear grad cache
            optimizer_parameters.zero_grad()
            optimizer_init_inventory.zero_grad()
            # Reset the sourcing model with the learned init inventory
            sourcing_model.reset()
            total_cost = self.get_total_cost(sourcing_model, sourcing_periods)
            total_cost.backward()
            # Gradient descend
            if epoch % 3 == 0:
                optimizer_init_inventory.step()
            else:
                optimizer_parameters.step()
            # Save the best model
            if validation_sourcing_periods is not None and epoch % 10 == 0:
                eval_cost = self.get_total_cost(
                    sourcing_model, validation_sourcing_periods
                )
                if eval_cost < min_cost:
                    min_cost = eval_cost
                    best_state = self.state_dict()
            else:
                if total_cost < min_cost:
                    min_cost = total_cost
                    best_state = self.state_dict()
            # Log train loss
            if tensorboard_writer is not None:
                tensorboard_writer.add_scalar(
                    "Avg. cost per period/train", total_cost / sourcing_periods, epoch
                )
                # Log evaluation loss
                if validation_sourcing_periods is not None and epoch % 10 == 0:
                    eval_cost = self.get_total_cost(
                        sourcing_model, validation_sourcing_periods
                    )
                    tensorboard_writer.add_scalar(
                        "Avg. cost per period/eval",
                        eval_cost / validation_sourcing_periods,
                        epoch,
                    )
                tensorboard_writer.flush()
        # Load the best model
        self.load_state_dict(best_state)

    def simulate(self, sourcing_model, sourcing_periods, seed=None):
        """
        Simulates the inventory and order quantities over a given number of sourcing periods.

        Parameters
        ----------
        sourcing_model : SourcingModel
            The sourcing model to be used for simulation.
        sourcing_periods : int
            The number of sourcing periods for simulation.
        seed : int, optional
            Random seed for reproducibility. Default is None.

        Returns
        -------
        tuple
            A tuple containing the past inventories and past orders as numpy arrays.
        """
        if seed is not None:
            torch.manual_seed(seed)
        sourcing_model.reset(batch_size=1)
        for i in range(sourcing_periods):
            current_inventory = sourcing_model.get_current_inventory()
            past_orders = sourcing_model.get_past_orders()
            q = self.forward(current_inventory, past_orders)
            sourcing_model.order(q)
        past_inventories = sourcing_model.get_past_inventories()[0, :].detach().numpy()
        past_orders = sourcing_model.get_past_orders()[0, :].detach().numpy()
        return past_inventories, past_orders

    def plot(self, sourcing_model, sourcing_periods):
        """
        Plots the inventory and order quantities over a given number of sourcing periods.

        Parameters
        ----------
        sourcing_model : SourcingModel
            The sourcing model to be used for plotting.
        sourcing_periods : int
            The number of sourcing periods for plotting.

        Returns
        -------
        None
        """
        past_inventories, past_orders = self.simulate(
            sourcing_model=sourcing_model, sourcing_periods=sourcing_periods
        )
        fig, ax = plt.subplots(ncols=2, figsize=(10, 4))

        ax[0].step(range(sourcing_periods), past_inventories[-sourcing_periods:])
        ax[0].yaxis.get_major_locator().set_params(integer=True)
        ax[0].set_title("Inventory")
        ax[0].set_xlabel("Period")
        ax[0].set_ylabel("Quantity")

        ax[1].step(range(sourcing_periods), past_orders[-sourcing_periods:])
        ax[1].yaxis.get_major_locator().set_params(integer=True)
        ax[1].set_title("Order")
        ax[1].set_xlabel("Period")
        ax[1].set_ylabel("Quantity")


class DualSourcingNeuralController(torch.nn.Module, NeuralControllerMixIn):
    """
    DualSourcingNeuralController is a neural network controller for dual sourcing inventory optimization.

    Parameters
    ----------
    hidden_layers : list
        List of integers specifying the sizes of hidden layers.
    activation : torch.nn.Module
        Activation function to be used in the hidden layers.
    compressed : bool
        Flag indicating whether the input is compressed.

    Attributes
    ----------
    hidden_layers : list
        List of integers specifying the sizes of hidden layers.
    activation : torch.nn.Module
        Activation function to be used in the hidden layers.
    compressed : bool
        Flag indicating whether the input is compressed.
    regular_lead_time : int
        Regular lead time.
    expedited_lead_time : int
        Expedited lead time.
    stack : torch.nn.Sequential
        Sequential stack of linear layers and activation functions.

    Methods
    -------
    init_layers(regular_lead_time, expedited_lead_time)
        Initialize the layers of the neural network.
    forward(current_inventory, past_orders)
        Forward pass of the neural network.
    get_total_cost(sourcing_model, sourcing_periods, seed=None)
        Calculate the total cost of the sourcing model.
    train(sourcing_model, sourcing_periods, epochs, validation_sourcing_periods=None, lr_init_inventory=1e-1, lr_parameters=3e-3, seed=None, tensorboard_writer=None)
        Train the neural network.
    simulate(sourcing_model, sourcing_periods, seed=None)
        Simulate the sourcing model using the neural network.
    plot(sourcing_model, sourcing_periods)
        Plot the inventory and order quantities.
    """

    def __init__(
        self,
        hidden_layers=[128, 64, 32, 16, 8, 4],
        activation=torch.nn.CELU(alpha=1),
        compressed=False,
    ):
        super().__init__()
        self.hidden_layers = hidden_layers
        self.activation = activation
        self.compressed = compressed
        self.lead_time = None
        self.stack = None

    def init_layers(self, regular_lead_time, expedited_lead_time):
        """
        Initialize the layers of the neural network.

        Parameters
        ----------
        regular_lead_time : int
            Regular lead time.
        expedited_lead_time : int
            Expedited lead time.

        Returns
        -------
        None
        """
        self.regular_lead_time = regular_lead_time
        self.expedited_lead_time = expedited_lead_time
        if self.compressed:
            input_length = regular_lead_time + expedited_lead_time
        else:
            input_length = regular_lead_time + expedited_lead_time + 1

        architecture = [
            torch.nn.Linear(input_length, self.hidden_layers[0]),
            self.activation,
        ]
        for i in range(len(self.hidden_layers)):
            if i < len(self.hidden_layers) - 1:
                architecture += [
                    torch.nn.Linear(self.hidden_layers[i], self.hidden_layers[i + 1]),
                    self.activation,
                ]
        architecture += [
            torch.nn.Linear(self.hidden_layers[-1], 2),
            torch.nn.ReLU(),
        ]
        self.stack = torch.nn.Sequential(*architecture)

    def forward(self, current_inventory, past_regular_orders, past_expedited_orders):
        """
        Forward pass of the neural network.

        Parameters
        ----------
        current_inventory : torch.Tensor
            Current inventory.
        past_regular_orders : torch.Tensor
            Past regular orders.
        past_expedited_orders : torch.Tensor
            Past expedited orders.

        Returns
        -------
        regular_q : torch.Tensor
            Regular order quantity.
        expedited_q : torch.Tensor
            Expedited order quantity.
        """
        if self.regular_lead_time > 0:
            if self.compressed:
                inputs = past_regular_orders[:, -self.regular_lead_time :]
                inputs[:, 0] += current_inventory
            else:
                inputs = torch.cat(
                    [
                        current_inventory,
                        past_regular_orders[:, -self.regular_lead_time :],
                    ],
                    dim=1,
                )

        if self.expedited_lead_time > 0:
            inputs = torch.cat(
                [inputs, past_expedited_orders[:, -self.expedited_lead_time :]], dim=1
            )

        h = self.stack(inputs)
        q = h - torch.frac(h).clone().detach()
        regular_q = q[:, [0]]
        expedited_q = q[:, [1]]
        return regular_q, expedited_q

    def get_total_cost(self, sourcing_model, sourcing_periods, seed=None):
        """
        Calculate the total cost of the sourcing model.

        Parameters
        ----------
        sourcing_model : Sourcing model.
            Sourcing model.
        sourcing_periods : int
            Number of sourcing periods.
        seed : int, optional
            Random seed for reproducibility.

        Returns
        -------
        total_cost : torch.Tensor
            Total cost.
        """
        if seed is not None:
            torch.manual_seed(seed)

        if self.lead_time is None:
            self.init_layers(
                regular_lead_time=sourcing_model.get_regular_lead_time(),
                expedited_lead_time=sourcing_model.get_expedited_lead_time(),
            )
        
        total_cost = 0
        for i in range(sourcing_periods):
            current_inventory = sourcing_model.get_current_inventory()
            past_regular_orders = sourcing_model.get_past_regular_orders()
            past_expedited_orders = sourcing_model.get_past_expedited_orders()
            regular_q, expedited_q = self.forward(
                current_inventory, past_regular_orders, past_expedited_orders
            )
            sourcing_model.order(regular_q, expedited_q)
            current_cost = sourcing_model.get_cost(regular_q, expedited_q)
            total_cost += current_cost.mean()
        return total_cost

    def train(
        self,
        sourcing_model,
        sourcing_periods,
        epochs,
        validation_sourcing_periods=None,
        lr_init_inventory=1e-1,
        lr_parameters=3e-3,
        seed=None,
        tensorboard_writer=None,
    ):
        """
        Train the neural network.

        Parameters
        ----------
        sourcing_model : Sourcing model
            Sourcing model.
        sourcing_periods : int
            Number of sourcing periods.
        epochs : int
            Number of training epochs.
        validation_sourcing_periods : int, optional
            Number of sourcing periods for validation.
        lr_init_inventory : float, optional
            Learning rate for initializing inventory.
        lr_parameters : float, optional
            Learning rate for neural network parameters.
        seed : int, optional
            Random seed for reproducibility.
        tensorboard_writer : TensorBoard writer, optional
            TensorBoard writer for logging.
        """
        if seed is not None:
            torch.manual_seed(seed)

        optimizer_init_inventory = torch.optim.RMSprop(
            [sourcing_model.init_inventory], lr=lr_init_inventory
        )
        optimizer_parameters = torch.optim.RMSprop(self.parameters(), lr=lr_parameters)
        min_cost = np.inf

        for epoch in range(epochs):
            # Clear grad cache
            optimizer_init_inventory.zero_grad()
            optimizer_parameters.zero_grad()
            # Reset the sourcing model with the learned init inventory
            sourcing_model.reset()
            total_cost = self.get_total_cost(sourcing_model, sourcing_periods)
            total_cost.backward()
            # Perform gradient descend
            if epoch % 3 == 0:
                optimizer_init_inventory.step()
            else:
                optimizer_parameters.step()
            # Save the best model
            if validation_sourcing_periods is not None and epoch % 10 == 0:
                eval_cost = self.get_total_cost(
                    sourcing_model, validation_sourcing_periods
                )
                if eval_cost < min_cost:
                    min_cost = eval_cost
                    best_state = self.state_dict()
            else:
                if total_cost < min_cost:
                    min_cost = total_cost
                    best_state = self.state_dict()
            # Log train loss
            if tensorboard_writer is not None:
                tensorboard_writer.add_scalar(
                    "Avg. cost per period/train", total_cost / sourcing_periods, epoch
                )
                # Log evaluation loss
                tensorboard_writer.add_scalar(
                    "Avg. cost per period/eval",
                    eval_cost / validation_sourcing_periods,
                    epoch,
                )
                tensorboard_writer.flush()

        self.load_state_dict(best_state)

    def simulate(self, sourcing_model, sourcing_periods, seed=None):
        """
        Simulate the sourcing model using the neural network.

        Parameters
        ----------
        sourcing_model : Sourcing model
            The sourcing model.
        sourcing_periods : int
            Number of sourcing periods.
        seed : int, optional
            Random seed for reproducibility.

        Returns
        -------
        past_inventories : list
            List of past inventories.
        past_regular_orders : list
            List of past regular orders.
        past_expedited_orders : list
            List of past expedited orders.

        """
        if seed is not None:
            torch.manual_seed(seed)
        sourcing_model.reset(batch_size=1)
        for i in range(sourcing_periods):
            current_inventory = sourcing_model.get_current_inventory()
            past_regular_orders = sourcing_model.get_past_regular_orders()
            past_expedited_orders = sourcing_model.get_past_expedited_orders()
            regular_q, expedited_q = self.forward(
                current_inventory, past_regular_orders, past_expedited_orders
            )
            sourcing_model.order(regular_q, expedited_q)
        past_inventories = sourcing_model.get_past_inventories()[0, :].detach().numpy()
        past_regular_orders = (
            sourcing_model.get_past_regular_orders()[0, :].detach().numpy()
        )
        past_expedited_orders = (
            sourcing_model.get_past_expedited_orders()[0, :].detach().numpy()
        )
        return past_inventories, past_regular_orders, past_expedited_orders

    def plot(self, sourcing_model, sourcing_periods):
        """
        Plot the inventory and order quantities.

        Parameters
        ----------
        sourcing_model : Sourcing model
            The sourcing model.
        sourcing_periods : int
            Number of sourcing periods.

        Returns
        -------
        None

        """
        past_inventories, past_regular_orders, past_expedited_orders = self.simulate(
            sourcing_model=sourcing_model, sourcing_periods=sourcing_periods
        )
        fig, ax = plt.subplots(ncols=2, figsize=(10, 4))
        ax[0].step(range(sourcing_periods), past_inventories[-sourcing_periods:])
        ax[0].yaxis.get_major_locator().set_params(integer=True)
        ax[0].set_title("Inventory")
        ax[0].set_xlabel("Period")
        ax[0].set_ylabel("Quantity")

        ax[1].step(
            range(sourcing_periods),
            past_expedited_orders[-sourcing_periods:],
            label="Expedited Order",
        )
        ax[1].step(
            range(sourcing_periods),
            past_regular_orders[-sourcing_periods:],
            label="Regular Order",
        )
        ax[1].yaxis.get_major_locator().set_params(integer=True)
        ax[1].set_title("Order")
        ax[1].set_xlabel("Period")
        ax[1].set_ylabel("Quantity")
        ax[1].legend()


class CappedDualIndexController:
    """
    Controller class for capped dual index inventory optimization.

    Parameters
    ----------
    s_e : int
        Capped dual index parameter 1
    s_r : int
        Capped dual index parameter 2
    q_r : int
        Capped dual index parameter 3

    Notes
    -----
    The function follows the implementation of Sun, J., & Van Mieghem, J. A. (2019)([1]_).

    References
    ----------
    .. [1] Robust dual sourcing inventory management: Optimality of capped dual index policies and smoothing.
           Manufacturing & Service Operations Management, 21(4), 912-931.
    """

    def __init__(self, s_e=0, s_r=0, q_r=0):
        self.s_e = s_e
        self.s_r = s_r
        self.q_r = q_r

    def capped_dual_index_sum(
        self,
        current_inventory,
        past_regular_orders,
        past_expedited_orders,
        regular_lead_time,
        expedited_lead_time,
        k,
    ):
        """
        Calculate the capped dual index sum.

        Parameters
        ----------
        current_inventory : int
            Current inventory level.
        past_regular_orders : numpy.ndarray
            Array of past regular orders.
        past_expedited_orders : numpy.ndarray
            Array of past expedited orders.
        regular_lead_time : int
            Regular lead time.
        expedited_lead_time : int
            Expedited lead time.
        k : int
            Parameter for capped dual index sum calculation.

        Returns
        -------
        int
            The capped dual index sum.
        """
        inventory_position = (
            current_inventory
            + past_regular_orders[
                :, -regular_lead_time : -regular_lead_time + k + 1
            ].sum()
        )
        if expedited_lead_time > max(1, expedited_lead_time - k):
            inventory_position += past_expedited_orders[
                -expedited_lead_time : -expedited_lead_time
                + min(k, expedited_lead_time - 1)
                + 1
            ].sum()
        return inventory_position

    def forward(
        self,
        current_inventory,
        past_regular_orders,
        past_expedited_orders,
        regular_lead_time,
        expedited_lead_time,
    ):
        """
        Perform forward calculation for capped dual index optimization.

        Parameters
        ----------
        current_inventory : int
            Current inventory level.
        past_regular_orders : numpy.ndarray
            Array of past regular orders.
        past_expedited_orders : numpy.ndarray
            Array of past expedited orders.
        regular_lead_time : int
            Regular lead time.
        expedited_lead_time : int
            Expedited lead time.

        Returns
        -------
        tuple
            A tuple containing the regular order quantity and expedited order quantity.
        """
        inventory_position = self.capped_dual_index_sum(
            current_inventory,
            past_regular_orders,
            past_expedited_orders,
            regular_lead_time,
            expedited_lead_time,
            k=0,
        )
        inventory_position_limit = self.capped_dual_index_sum(
            current_inventory,
            past_regular_orders,
            past_expedited_orders,
            regular_lead_time,
            expedited_lead_time,
            k=regular_lead_time - expedited_lead_time - 1,
        )
        regular_q = min(max(0, self.s_r - inventory_position_limit), self.q_r)
        expedited_q = max(0, self.s_e - inventory_position)
        return regular_q, expedited_q

    def get_total_cost(self, sourcing_model, sourcing_periods, seed=None):
        """
        Calculate the total cost for capped dual index optimization.

        Parameters
        ----------
        sourcing_model : SourcingModel
            The sourcing model.
        sourcing_periods : int
            Number of sourcing periods.
        seed : int, optional
            Random seed for reproducibility.

        Returns
        -------
        float
            The total cost.
        """
        if seed is not None:
            torch.manual_seed(seed)
        regular_lead_time = sourcing_model.get_regular_lead_time()
        expedited_lead_time = sourcing_model.get_expedited_lead_time()
        total_cost = 0
        for i in range(sourcing_periods):
            current_inventory = sourcing_model.get_current_inventory()
            past_regular_orders = sourcing_model.get_past_regular_orders()
            past_expedited_orders = sourcing_model.get_past_expedited_orders()
            regular_q, expedited_q = self.forward(
                current_inventory,
                past_regular_orders,
                past_expedited_orders,
                regular_lead_time,
                expedited_lead_time,
            )
            sourcing_model.order(regular_q, expedited_q)
            current_cost = sourcing_model.get_cost(regular_q, expedited_q)
            total_cost += current_cost
        return total_cost

    def train(
        self,
        sourcing_model,
        sourcing_periods,
        s_e_range=np.arange(2, 11),
        s_r_range=np.arange(2, 11),
        q_r_range=np.arange(2, 11),
        seed=None,
    ):
        """
        Train the capped dual index controller.

        Parameters
        ----------
        sourcing_model : SourcingModel
            The sourcing model.
        sourcing_periods : int
            Number of sourcing periods.
        s_e_range : numpy.ndarray, optional
            Range of values for s_e.
        s_r_range : numpy.ndarray, optional
            Range of values for s_r.
        q_r_range : numpy.ndarray, optional
            Range of values for q_r.
        seed : int, optional
            Random seed for reproducibility.
        """
        if seed is not None:
            torch.manual_seed(seed)
        min_cost = np.inf
        for s_e in s_e_range:
            for s_r in s_r_range:
                for q_r in q_r_range:
                    sourcing_model.reset()
                    self.s_e = s_e
                    self.s_r = s_r
                    self.q_r = q_r
                    total_cost = self.get_total_cost(sourcing_model, sourcing_periods)
                    if total_cost < min_cost:
                        min_cost = total_cost
                        s_e_optimal = s_e
                        s_r_optimal = s_r
                        q_r_optimal = q_r
        self.s_e = s_e_optimal
        self.s_r = s_r_optimal
        self.q_r = q_r_optimal

    def simulate(self, sourcing_model, sourcing_periods, seed=None):
        """
        Simulate the capped dual index controller.

        Parameters
        ----------
        sourcing_model : SourcingModel
            The sourcing model.
        sourcing_periods : int
            Number of sourcing periods.
        seed : int, optional
            Random seed for reproducibility.

        Returns
        -------
        tuple
            A tuple containing the past inventories, past regular orders, and past expedited orders.
        """
        if seed is not None:
            torch.manual_seed(seed)
        sourcing_model.reset()
        regular_lead_time = sourcing_model.get_regular_lead_time()
        expedited_lead_time = sourcing_model.get_expedited_lead_time()
        for i in range(sourcing_periods):
            current_inventory = sourcing_model.get_current_inventory()
            past_regular_orders = sourcing_model.get_past_regular_orders()
            past_expedited_orders = sourcing_model.get_past_expedited_orders()
            regular_q, expedited_q = self.forward(
                current_inventory,
                past_regular_orders,
                past_expedited_orders,
                regular_lead_time,
                expedited_lead_time,
            )
            sourcing_model.order(regular_q, expedited_q)
        past_inventories = sourcing_model.get_past_inventories()[0, :].detach().numpy()
        past_regular_orders = (
            sourcing_model.get_past_regular_orders()[0, :].detach().numpy()
        )
        past_expedited_orders = (
            sourcing_model.get_past_expedited_orders()[0, :].detach().numpy()
        )
        return past_inventories, past_regular_orders, past_expedited_orders

    def plot(self, sourcing_model, sourcing_periods):
        """
        Plot the simulation results.

        Parameters
        ----------
        sourcing_model : SourcingModel
            The sourcing model.
        sourcing_periods : int
            Number of sourcing periods.
        """
        past_inventories, past_regular_orders, past_expedited_orders = self.simulate(
            sourcing_model=sourcing_model, sourcing_periods=sourcing_periods
        )
        fig, ax = plt.subplots(ncols=2, figsize=(10, 4))
        ax[0].step(range(sourcing_periods), past_inventories[-sourcing_periods:])
        ax[0].yaxis.get_major_locator().set_params(integer=True)
        ax[0].set_title("Inventory")
        ax[0].set_xlabel("Period")
        ax[0].set_ylabel("Quantity")

        ax[1].step(
            range(sourcing_periods),
            past_expedited_orders[-sourcing_periods:],
            label="Expedited Order",
        )
        ax[1].step(
            range(sourcing_periods),
            past_regular_orders[-sourcing_periods:],
            label="Regular Order",
        )
        ax[1].yaxis.get_major_locator().set_params(integer=True)
        ax[1].set_title("Order")
        ax[1].set_xlabel("Period")
        ax[1].set_ylabel("Quantity")
        ax[1].legend()
