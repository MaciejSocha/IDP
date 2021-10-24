import random


class Neuron:
    number_of_inputs = None
    list_of_weights = []
    list_of_inputs = []

    def __init__(self, number_of_inputs):
        self.number_of_inputs = number_of_inputs
        self.list_of_weights = []
        self.list_of_inputs = [None] * number_of_inputs

        for i in range(number_of_inputs):
            self.list_of_weights.append(random.random())

    def set_inputs(self, list_of_number):
        if len(list_of_number) != self.number_of_inputs & len(list_of_number) != len(self.list_of_inputs):
            raise Exception

        for i in range(len(list_of_number)):
            self.list_of_inputs[i] = list_of_number[i]

    def process(self):
        result = 0
        for i in range(self.number_of_inputs):
            result += self.list_of_inputs[i] * self.list_of_weights[i]
        return result

    def set_random_weights(self):
        for i in range(len(self.list_of_weights)):
            self.list_of_weights[i] = random.random()
