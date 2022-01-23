import random


def mute(probability, population):
    p = []

    for i in range(len(population)):
        for j in range(len(population[i])):
            rng = random.uniform(0, 1)
            if rng < probability:
                # print('mutation! chromosome: ', i, 'bit ', j)
                if population[i][j] == '0':
                    population[i] = population[i][:j] + '1' + population[i][j+1:]
                else:
                    population[i] = population[i][:j] + '0' + population[i][j+1:]
    return population
