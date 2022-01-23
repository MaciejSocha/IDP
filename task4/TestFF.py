import matplotlib.pyplot as plt
import FitnessFunction


def testFF():
    print("hello there")
    start = 0.5
    end = 2.5
    step = 0.01

    vals = []
    iks = []
    i = start
    while i <= end:
        iks.append(i)
        vals.append(FitnessFunction.function(i))
        i += step

    plt.plot(iks, vals)
    plt.grid(True)
    plt.show()
    print('done')


testFF()
