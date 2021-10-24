import Train
from Neuron import Neuron

if __name__ == '__main__':
    neuron = Neuron(2)
    list_input = [1, 2]
    neuron.set_inputs(list_input)
    print(neuron.process())
    tr_set = [3, 8]
    tr_set_out = 24
    Train.training_single_pattern(neuron, 500, 0.001, tr_set, tr_set_out)
    neuron.set_inputs([2, 6])
    print(neuron.process())
