import os
import random

from deap import creator, base, tools, algorithms

# single objective fitness
creator.create("FitnessMin", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)


toolbox = base.Toolbox()
## random generate freqeuncy between 2 and 6
# toolbox.register("attr_bool", random.randint, 3, 6)
toolbox.register("attr_bool", random.uniform,2,6)
# there are 4 lines 
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=4)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalOneMax(individual):
    # print(individual)
    # os.system("pause")
    return sum(individual),

toolbox.register("evaluate", evalOneMax)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

population = toolbox.population(n=10)
for p in population:
    print(p)

NGEN=5
for gen in range(NGEN):
    offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)
    fits = toolbox.map(toolbox.evaluate, offspring)
    for fit, ind in zip(fits, offspring):
        ind.fitness.values = fit
    population = toolbox.select(offspring, k=len(population))
top10 = tools.selBest(population, k=10)
