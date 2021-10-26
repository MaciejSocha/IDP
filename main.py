import Train
from Neuron import Neuron

if __name__ == '__main__':
    # neuron = Neuron(5)
    # train = [5, 10, 15, 20, 25]
    # test = 75
    # Train.training_single_pattern(neuron, 50, 0.001, train, test, False)
    # neuron.set_inputs(train)
    # print(neuron.process())
    #
    # print('nulti')
    neuron = Neuron(5)
    train_3 = [[1, 2, 3, 4, 5], [10, 11, 12, 13, 14], [20, 21, 22, 23, 24]]
    test_3 = [15, 60, 110]
    train_5 = [[1, 2, 3, 4, 5], [10, 11, 12, 13, 14], [20, 21, 22, 23, 24], [30, 31, 32, 33, 34], [40, 41, 42, 43, 44]]
    test_5 = [15, 60, 110, 160, 210]
    train_7 = [[1, 2, 3, 4, 5], [10, 11, 12, 13, 14], [20, 21, 22, 23, 24], [30, 31, 32, 33, 34], [40, 41, 42, 43, 44],
               [50, 51, 52, 53, 54], [60, 61, 62, 63, 64]]
    test_7 = [15, 60, 110, 160, 210, 260, 310]
    Train.training_multi_patterns(neuron, 500, 0.0001, train_7, test_7)
    neuron.set_inputs([1, 2, 3, 4, 5])
    print(neuron.process())
    neuron.set_inputs([10, 11, 12, 13, 14])
    print(neuron.process())
    neuron.set_inputs([20, 21, 22, 23, 24])
    print(neuron.process())
    neuron.set_inputs([30, 31, 32, 33, 34])
    print(neuron.process())
    neuron.set_inputs([40, 41, 42, 43, 44])
    print(neuron.process())
    neuron.set_inputs([50, 51, 52, 53, 54])
    print(neuron.process())
    neuron.set_inputs([60, 61, 62, 63, 64])
    print(neuron.process())
