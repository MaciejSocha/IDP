import math

from task2 import Function
from task2.InputLayer import InputLayer
from task2.Layer import Layer


class Network:
    def __init__(self, input_layer_size, hidden_layer_size, output_layer_size, bias):
        self.inp_size = input_layer_size
        self.hid_size = hidden_layer_size
        self.out_size = output_layer_size
        self.bias = bias
        self.outputs_values = []

        self.input_layer = InputLayer(input_layer_size, hidden_layer_size)
        self.hidden_layer = Layer(hidden_layer_size, input_layer_size, 'sigmoid', bias)
        self.output_layer = Layer(output_layer_size, hidden_layer_size, 'sigmoid', bias)

        for i in range(output_layer_size):
            self.outputs_values.append(0)

    def process(self, list_inputs):
        if len(list_inputs) != self.inp_size:
            raise Exception("Size of inputs not equal to number of neurons in input layer!")
        # Input Layer processing
        self.input_layer.process(list_inputs)
        outputs_from_input_layer = self.input_layer.values_outputs
        # print("Outputs for input layer: ", outputs_from_input_layer)
        # Hidden Layer processing
        self.hidden_layer.process(outputs_from_input_layer)
        outputs_from_hidden_layer = self.hidden_layer.values_outputs
        # print("Outputs for hidden layer: ", outputs_from_hidden_layer)
        # Output Layer processing
        self.output_layer.process(outputs_from_hidden_layer)
        self.outputs_values = self.output_layer.values_outputs
        # print("Outputs for output layer: ", self.outputs_values)
        return self.outputs_values

    def learn(self, list_inputs, list_output, training_step):
        outputs = self.process(list_inputs)
        # calculating deltas
        deltas_output_layer = []
        for i in range(len(outputs)):
            deltas_output_layer.append((Function.calc_derivative_by_name(self.output_layer.activation_function, self.output_layer.neurons[i].calc())) * (list_output[i] - outputs[i]))
        # print("deltas_output_layer", deltas_output_layer)

        deltas_hidden_layer = []
        for i in range(len(self.hidden_layer.neurons)):
            temp_sum = 0
            for j in range(len(self.output_layer.neurons)):
                temp_sum += deltas_output_layer[j] * self.output_layer.neurons[j].list_of_weights[i]
            # if self.bias:
                # temp_sum += deltas_output_layer[j] * self.output_layer.neurons[j].bias_weight
            deltas_hidden_layer.append((Function.calc_derivative_by_name(self.hidden_layer.activation_function, self.hidden_layer.neurons[i].calc())) * (temp_sum))
        # print("deltas_hidden_layer", deltas_hidden_layer)

        # calc error
        squared_error = 0
        for i in range(len(self.output_layer.neurons)):
            squared_error += math.pow((list_output[i] - outputs[i]), 2)
        squared_error = squared_error / len(self.output_layer.neurons)


        # change weights
        for i in range(len(self.output_layer.neurons)):
            for j in range(len(self.output_layer.neurons[i].list_of_inputs)):
                self.output_layer.neurons[i].list_of_weights[j] += (training_step * deltas_output_layer[i] * self.output_layer.neurons[i].list_of_inputs[j])
            if self.bias:
                self.output_layer.neurons[i].bias_weight += (training_step * deltas_output_layer[i])

        for i in range(len(self.hidden_layer.neurons)):
            for j in range(len(self.hidden_layer.neurons[i].list_of_inputs)):
                self.hidden_layer.neurons[i].list_of_weights[j] += (training_step * deltas_hidden_layer[i] * self.hidden_layer.neurons[i].list_of_inputs[j])
            if self.bias:
                self.hidden_layer.neurons[i].bias_weight += (training_step * deltas_hidden_layer[i])

        return squared_error
