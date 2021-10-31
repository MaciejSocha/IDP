import Train
from task1.Neuron import Neuron

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
    train_3 = [[18, 16, 17, 19, 13], [21, 28, 23, 25, 24], [10, 20, 19, 28, 12]]
    test_3 = [16.6, 24.2, 17.8]
    train_5 = [[18, 16, 17, 19, 13], [21, 28, 23, 25, 24], [10, 20, 19, 28, 12], [31, 39, 33, 32, 38],
               [39, 15, 27, 15, 34]]
    test_5 = [16.6, 24.2, 17.8, 34.6, 26]
    train_7 = [[18, 16, 17, 19, 13], [21, 28, 23, 25, 24], [10, 20, 19, 28, 12], [31, 39, 33, 32, 38],
               [39, 15, 27, 15, 34], [45, 48, 43, 44, 41], [11, 50, 48, 35, 24]]
    test_7 = [16.6, 24.2, 17.8, 34.6, 26, 44.2, 33.6]
    Train.training_multi_patterns(neuron, 500, 0.0001, train_7, test_7, False)

    neuron.set_inputs([18, 16, 17, 19, 13])
    print('calculated output: ', neuron.process(), '    desired output: ', 16.6)
    neuron.set_inputs([21, 28, 23, 25, 24])
    print('calculated output: ', neuron.process(), '    desired output: ', 24.2)
    neuron.set_inputs([10, 20, 19, 28, 12])
    print('calculated output: ', neuron.process(), '    desired output: ', 17.8)
    neuron.set_inputs([31, 39, 33, 32, 38])
    print('calculated output: ', neuron.process(), '    desired output: ', 34.6)
    neuron.set_inputs([39, 15, 27, 15, 34])
    print('calculated output: ', neuron.process(), '    desired output: ', 26)
    neuron.set_inputs([45, 48, 43, 44, 41])
    print('calculated output: ', neuron.process(), '    desired output: ', 44.2)
    neuron.set_inputs([11, 50, 48, 35, 24])
    print('calculated output: ', neuron.process(), '    desired output: ', 33.6)
