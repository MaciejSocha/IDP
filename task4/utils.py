import math
import FitnessFunction


def calc_bits(number):
    n = 1
    while True:
        tmp = math.pow(2, n)
        if tmp >= number:
            return n
        n += 1


def make_decimal(binary, bits, start, length):
    i = 0
    sums = 0
    for bit in reversed(binary):
        sums += math.pow(2, i) * int(bit)
        i += 1
    return start + ((length * sums) / (math.pow(2, bits) - 1))


def eval_binary(binary, bits, start, length):
    mkdec = make_decimal(binary, bits, start, length)
    return FitnessFunction.function(mkdec)


def calc_average_ff(eval_population):
    ss = 0
    for i in range(len(eval_population)):
        ss += eval_population[i]

    return ss / len(eval_population)
