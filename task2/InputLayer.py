from task2.Perceptron import Perceptron


class InputLayer:
    number_of_neurons = 0
    neurons = []

    def __init__(self, number_of_neurons):
        self.number_of_neurons = number_of_neurons

        for i in range(len(number_of_neurons)):
            self.neurons.append(Perceptron(1, 'linear', False))
