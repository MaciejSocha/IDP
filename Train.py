import math


def training_single_pattern(neuron, epoch, n, training_set, training_set_output, breaking):
    # just in case the weights aren't randomize
    neuron.set_random_weights()
    for k in range(epoch):
        neuron.set_inputs(training_set)
        y = neuron.process()
        delta = training_set_output - y
        # print(delta)
        if (math.fabs(delta) < 0.0001) & breaking == True:
            print('STOP at epoch: ', k)
            return
        for j in range(len(neuron.list_of_inputs)):
            neuron.list_of_weights[j] = neuron.list_of_weights[j] + (n * delta) * neuron.list_of_inputs[j]


def training_multi_patterns(neuron, epoch, n, training_set, training_set_output):
    # just in case the weights aren't randomize
    neuron.set_random_weights()
    for k in range(epoch):
        for i in range(len(training_set)):
            neuron.set_inputs(training_set[i])
            y = neuron.process()
            delta = training_set_output[i] - y
            # print(delta)
            if math.fabs(delta) < 0.0001:
                print('STOP at epoch: ', k)
                return
            for j in range(len(neuron.list_of_inputs)):
                neuron.list_of_weights[j] = neuron.list_of_weights[j] + (n * delta) * neuron.list_of_inputs[j]
