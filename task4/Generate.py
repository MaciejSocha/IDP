import random


def random_chromosome(n_bits):
    chromosome = ''
    for n in range(n_bits):
        temp = random.randint(0, 100)
        if temp % 2 == 0:
            chromosome += '1'
        else:
            chromosome += '0'
    return chromosome


def random_many_chromosomes(n_bits, n_chromosomes):
    chromosomes = []
    for n in range(n_chromosomes):
        chromosomes.append(random_chromosome(n_bits))
    return chromosomes
