import random

from task2 import Function


class Perceptron:
    def __init__(self, number_of_inputs, activation_function, bias, is_input):
        self.number_of_inputs = number_of_inputs
        self.activation_function = activation_function
        self.bias = bias
        self.is_input = is_input
        self.list_of_weights = []
        self.list_of_inputs = []
        self.bias_weight = None

        if not is_input:
            for i in range(number_of_inputs):
                self.list_of_weights.append(random.random())
                self.list_of_inputs.append(0)
            if bias:
                self.bias_weight = random.random()
        else:
            for i in range(number_of_inputs):
                self.list_of_weights.append(1)
                self.list_of_inputs.append(0)
            if bias:
                self.bias_weight = 1

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
        else:
            if self.activation_function == 'linear':
                for i in range(self.number_of_inputs):
                    result += Function.linear(self.list_of_inputs[i] * self.list_of_weights[i])
            else:
                raise Exception

        if self.bias:
            result += 1 * self.bias_weight

        return result
