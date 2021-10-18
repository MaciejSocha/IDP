def training(neuron, epoch, n, training_set, training_set_outputs):
    # just in case the weights aren't randomize
    neuron.set_random_weights()
    for k in range(epoch):
        for i in range(len(training_set)):
            neuron.set_inputs(training_set[i])
            r = neuron.process()
            delta = training_set_outputs[i] - r
