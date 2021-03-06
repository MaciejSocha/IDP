import math


def sigmoid(x):
    return 1 / (1 + math.pow(math.e, -x))


def sigmoid_derivative(x):
    return (math.pow(math.e, -x)) / (math.pow((1 + math.pow(math.e, -x)), 2))


def linear(x):
    return x


def linear_derivative(x):
    return x


def calc_derivative_by_name(name, x):
    ret = 0.0
    if name == 'sigmoid':
        ret = sigmoid_derivative(x)
    else:
        if name == 'linear':
            ret = linear_derivative(x)
    return ret

