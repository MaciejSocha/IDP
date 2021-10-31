import math


def sigmoid(x):
    return 1/(1 + math.pow(math.e, -x))


def sigmoid_derivative(x):
    return (math.pow(math.e, -x))/(math.pow((1 + math.pow(math.e, -x)), 2))


def linear(x):
    return x


def linear_derivative(x):
    return x
