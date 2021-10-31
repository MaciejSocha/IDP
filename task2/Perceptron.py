import random

from task2 import Function


class Perceptron:
    number_of_inputs = 0
    list_of_weights = []
    list_of_inputs = []
    activation_function = 'sigmoid'
    bias = False
    bias_weight = None

    def __init__(self, number_of_inputs, activation_function, bias):
        self.number_of_inputs = number_of_inputs
        self.activation_function = activation_function
        self.bias = bias

        for i in range(number_of_inputs):
            self.list_of_weights.append(random.random())
        if bias:
            self.bias_weight = random.random()

    def set_inputs(self, list_of_numbers):
        if len(list_of_numbers) != self.number_of_inputs & len(list_of_numbers) != len(self.list_of_inputs):
            raise Exception

        for i in range(len(list_of_numbers)):
            self.list_of_inputs[i] = list_of_numbers[i]

    def process(self):
        result = 0
        if self.activation_function == 'sigmoid':
            for i in range(self.number_of_inputs):
                result += Function.sigmoid(self.list_of_inputs[i] * self.list_of_weights[i])
        if self.activation_function == 'linear':
            for i in range(self.number_of_inputs):
                result += Function.linear(self.list_of_inputs[i] * self.list_of_weights[i])
        else:
            raise Exception

        if self.bias:
            result += 1 * self.bias_weight

        return result
