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
        print("Outputs for input layer: ", outputs_from_input_layer)
        # Hidden Layer processing
        self.hidden_layer.process(outputs_from_input_layer)
        outputs_from_hidden_layer = self.hidden_layer.values_outputs
        print("Outputs for hidden layer: ", outputs_from_hidden_layer)
        # Output Layer processing
        self.output_layer.process(outputs_from_hidden_layer)
        self.outputs_values = self.output_layer.values_outputs
        print("Outputs for output layer: ", self.outputs_values)
        return self.outputs_values
