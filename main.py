import Train
from Neuron import Neuron

if __name__ == '__main__':
    neuron = Neuron(2)
    train = [1, 2]
    test = 3
    Train.training_single_pattern(neuron, 500, 0.0001, train, test)
    neuron.set_inputs([2, 3])
    print(neuron.process())

    print('nulti')
    neuron = Neuron(2)
    train = [[1, 2], [2, 3], [3, 4]]
    test = [3, 6, 7]
    Train.training_multi_patterns(neuron, 500, 0.0001, train, test)
    neuron.set_inputs([4, 5])
    print(neuron.process())
