from task2.Network import Network

if __name__ == '__main__':
    net = Network(4, 2, 4, True)
    print(net.process([1, 2, 3, 4]))
