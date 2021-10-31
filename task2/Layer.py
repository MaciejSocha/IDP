class Layer:
    number_of_neurons = 0
    activation_function = 'sigmoid'
    bias = False

    def __init__(self, number_of_neurons, activation_function, bias):
        self.number_of_neurons = number_of_neurons
        self.activation_function = activation_function
        self.bias = bias
