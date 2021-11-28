from task2.Perceptron import Perceptron


class Layer:
    def __init__(self, number_of_neurons, number_of_inputs, activation_function, bias):
        self.number_of_neurons = number_of_neurons
        self.number_of_inputs = number_of_inputs
        self.activation_function = activation_function
        self.bias = bias
        self.neurons = []
        self.values_outputs = []

        for i in range(number_of_neurons):
            self.neurons.append(Perceptron(number_of_inputs, activation_function, bias, False))
            self.values_outputs.append(0)

    def process(self, list_inputs):
        if len(list_inputs) != self.number_of_inputs:
            raise Exception("Size of inputs not equal to number of neurons in layer!")

        for i in range(len(self.neurons)):
            self.neurons[i].set_inputs(list_inputs)
            self.values_outputs[i] = self.neurons[i].process()
