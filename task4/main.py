import math
import utils
import Generate
import roulette
import crossing
import mutation
import matplotlib.pyplot as plt

if __name__ == '__main__':
    print("hello there")
    # start value
    a = 0.5
    # end value
    b = 2.5
    # precision
    p = 5
    # population size
    pop_size = 100
    # crossing probability
    pc = 0.35
    # mutation probability
    pm = 0.01
    # no iters
    generations = 1000

    length = b - a
    # print('length ', length)
    precision = length * math.pow(10, p)
    # print('parts ', precision)
    bits = utils.calc_bits(precision)
    print('bits ', bits)

    initial_pop = Generate.random_many_chromosomes(bits, pop_size)
    ev1 = []
    for g in range(len(initial_pop)):
        ev1.append(utils.eval_binary(initial_pop[g], bits, a, length))
    # print('ini_pop     : ', initial_pop)
    # print('ini_pop_eval: ', ev1)
    old_pop = initial_pop
    vgs = []
    vks = []
    deltas = []
    prev = 0
    for i in range(generations):
        new_pop = roulette.calc(old_pop, bits, a, length)
        crossed_pop = crossing.cross(pc, new_pop)
        mutated_pop = mutation.mute(pm, crossed_pop)
        old_pop = mutated_pop

        evaluated = []
        iks = []
        for h in range(len(old_pop)):
            evaluated.append(utils.eval_binary(old_pop[h], bits, a, length))
            iks.append(utils.make_decimal(old_pop[h], bits, a, length))
        # print('end_pop_eval: ', evaluated)
        # print('end_pop_iks: ', iks)
        vgs.append(utils.calc_average_ff(evaluated))
        vks.append(utils.calc_average_ff(iks))
        # print('avg_evaluation: ', utils.calc_average_ff(evaluated))
        # print('avg_iks: ', utils.calc_average_ff(iks))
        deltas.append(utils.calc_average_ff(iks) - 2.45056)
        print('DELTA: ', (utils.calc_average_ff(iks) - 2.45056))
        if math.fabs(utils.calc_average_ff(iks) - prev) < 0.0001:
            print('BREAK')
            break
        prev = utils.calc_average_ff(iks)

    plt.plot(vks)
    plt.axhline(y=2.45056, color='r', linestyle='-')
    plt.show()

    plt.plot(vgs)
    plt.axhline(y=10.1388, color='r', linestyle='-')
    plt.show()

    plt.plot(deltas)
    plt.show()
