from task2.Network import Network
import random


def training(training_step, n_epoch, training_patterns, training_outputs, network):
    for i in range(n_epoch):
        temp_iterators = [it for it in range(len(training_patterns))]
        random.shuffle(temp_iterators)
        for j in temp_iterators:
            # print("training pattern:                 ", training_patterns[j])
            # print("testing  pattern:                 ", training_outputs[j])
            print(network.learn(training_patterns[j], training_outputs[j], training_step))


if __name__ == '__main__':
    net = Network(4, 2, 4, True)
    net2 = Network(4, 2, 4, True)
    # print(net.process([1, 0, 0, 0]))
    print("learn")
    # print(net.learn([1, 0, 0, 0], [1, 0, 0, 0], 0.001))
    # for i in range(100000):
    #     print("Before change results:")
    #     print(net.learn([1, 0, 1, 0], [1, 1, 0, 0], 0.01))

    input_list1 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    input_list2 = [[0, 0, 0, 1]]
    in_out_list1 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    in_out_list2 = [[0, 0, 0, 1]]

    training(0.1, 10000, input_list1, in_out_list1, net)
    # training(0.01, 10000, input_list2, in_out_list2, net2)

    print("test")
    print(net.process([1, 0, 0, 0]))
    print(net.process([0, 1, 0, 0]))
    print(net.process([0, 0, 1, 0]))
    print(net.process([0, 0, 0, 1]))

    # print("test2")
    # print(net2.process([0, 0, 0, 1]))

