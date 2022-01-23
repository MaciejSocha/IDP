import utils
import random


def calc(population, bits, start, length):
    all_sum = 0
    probability = []
    distribuante = []
    for chromosome in population:
        all_sum += utils.eval_binary(chromosome, bits, start, length)
    for chromosome in population:
        probability.append(utils.eval_binary(chromosome, bits, start, length) / all_sum)
    for i in range(len(population)):
        tmp = 0
        for j in range(i + 1):
            tmp += probability[j]
        distribuante.append(tmp)
    # print('roulette results')
    # print('probs ', probability)
    # print('distribuantes', distribuante)

    new_population = []
    for i in range(len(population)):
        rng = random.uniform(0, 1)
        # print('random value', rng)
        ch = distribuante[0]
        j = 0
        for j in range(len(distribuante)):
            if rng >= ch:
                ch = distribuante[j]
            else:
                if j != 0:
                    j -= 1
                break
        # print('choose chromose: ', j)
        new_population.append(population[j])

    return new_population
