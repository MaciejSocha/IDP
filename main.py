from Neuron import Neuron

if __name__ == '__main__':
    neuron = Neuron(5)
    list_input = [1, 2, 3, 2, 1]
    neuron.set_inputs(list_input)
    print(neuron.process())
