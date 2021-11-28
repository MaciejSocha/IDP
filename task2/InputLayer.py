from task2.Perceptron import Perceptron


class InputLayer:
    def __init__(self, number_of_neurons, number_of_outputs):
        self.number_of_neurons = number_of_neurons
        self.number_of_outputs = number_of_outputs
        self.neurons = []
        self.values_outputs = []

        for i in range(number_of_neurons):
            self.neurons.append(Perceptron(1, 'linear', False, True))
            self.values_outputs.append(0)

    def process(self, list_inputs):
        if len(list_inputs) != self.number_of_neurons:
            raise Exception("Size of inputs not equal to number of neurons in input layer!")
        for i in range(len(self.neurons)):
            self.neurons[i].set_inputs([list_inputs[i]])
            self.values_outputs[i] = self.neurons[i].process()
