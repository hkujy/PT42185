"""
    The code is created to test the ga algorithm in python
"""
import array
import random

import numpy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

# create max fitness, weight = (1.0,) implies single objective optimization
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
# create Individual, which is list, and the first nes
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

# Attribute generator
# attribute_bool will generate a number betwen 4 and 10
toolbox.register("attr_bool", random.randint, 0, 1)

# Structure initializers
# define how to init a individual 
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, 100)
# based on the init for individual, initialize a population
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalOneMax(individual):
    return sum(individual),

# define evaluation method
toolbox.register("evaluate", evalOneMax)
# define cross over and mutation operation
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    random.seed(64)
    #population is register  
    pop = toolbox.population(n=100)  
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit  in zip(pop, fitnesses):
        ind.fitness.values = fit
    CXPB, MUTPB = 0.5, 0.2

    fits = [ind.fitness.values[0] for ind in pop]
    g = 0
    while max(fits) < 100 and g < 1000:
        g = g + 1
        print(" --- Generation %i ----" % g)
        # select the net generation individual
        offspring = toolbox.select(pop, len(pop))


    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)
    
    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=40, 
                                   stats=stats, halloffame=hof, verbose=True)
    
    return pop, log, hof

if __name__ == "__main__":
    main()