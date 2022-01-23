import random


def cross(probability, population):
    crossing_tab = []
    lens = (len(population))
    c = 0
    while c < lens:
        rng = random.uniform(0, 1)
        if rng < probability:
            crossing_tab.append(population[c])
            del population[c]
            lens -= 1
        c += 1

    if len(crossing_tab) == 1:
        population.append(crossing_tab[0])
        print('No one crossed')
        return population

    if len(crossing_tab) == 0:
        return population

    if len(crossing_tab) % 2 != 0:
        rng = random.randint(0, len(crossing_tab)-1)
        population.append(crossing_tab[rng])
        del crossing_tab[rng]
    # indexes = []
    # [indexes.append(i) for i in range(len(crossing_tab))]
    random.shuffle(crossing_tab)
    bits = len(crossing_tab[0])
    i = 0
    while i < len(crossing_tab):
        rngs = random.randint(1, bits - 1)
        # print('crossing chromosomes: ', crossing_tab[i], ', ', crossing_tab[i+1], 'random bit ', rngs)
        temp1_beg = crossing_tab[i][:rngs]
        temp1_end = crossing_tab[i][rngs:]
        temp2_beg = crossing_tab[i+1][:rngs]
        temp2_end = crossing_tab[i+1][rngs:]
        new1 = temp1_beg + temp2_end
        new2 = temp2_beg + temp1_end
        population.append(new1)
        population.append(new2)
        # print('after crossing: ', new1, ', ', new2)
        i += 2

    return population
