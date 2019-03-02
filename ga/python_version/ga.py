"""
    The code is created to test the ga algorithm in python
"""
import lower_level
import array
import random
import numpy
import math
import os
import matplotlib.pyplot as plt
from deap import algorithms
from deap import base
from deap import creator
from deap import tools


# parameters 
nvars = 4  # number of lines = number frequency to be designed
nbit_per_var = 8  # number of bits per decision variable
lb = [3,3,3,3]  # lower bound for freuqency： 3 veh /per hour
ub = [15,15,15,15] # upper bound for the frequency: 15 veh/hour

# GA parameters 
npop = 10  # population size 
ngen = 25  # number of generations
crossover_rate = 0.8
mutation_rate = 0.2



# create min fitness, weight = (1.0,) implies single objective optimization
# weight = -1 means that it is a minimization problem 
# if weight = 1, it means that is a maximization problem
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

# Attribute generator
# attribute_bool will generate a number betwen 4 and 10 
toolbox.register("attr_bool", random.randint, 0, 1)

# Structure initializers
# define how to init a individual 
# n= 4 means there are four transit lines
toolbox.register("individual", tools.initRepeat, creator.Individual,
 toolbox.attr_bool, n = nvars*nbit_per_var)
# based on the init for individual, initialize a population
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


def get_fitness(individual):
    # Step 1: decode binary representation to float decision variables
    fre = decode(individual,nbit_per_var,nvars,lb,ub)
    # Step 2: solve lower level assignment model
    res =  lower_level.assignment(fre)
    # return the objective function as the lower level solution
    return res.fun,

# define evaluation method
toolbox.register("evaluate", get_fitness)
# define cross over and mutation operation
toolbox.register("mate", tools.cxOnePoint)
toolbox.register("mutate", tools.mutFlipBit, indpb = mutation_rate)
toolbox.register("select", tools.selTournament, tournsize = 3)

def main():
    """
        main program for the GA
    """
    random.seed(64)
    # step 1: create the population
    pop = toolbox.population(n = npop)  
    # step 2: evaluate the population
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit  in zip(pop, fitnesses):
        # ind.fitness.values = fit
        ind.fitness.values = fit

    fits = [ind.fitness.values[0] for ind in pop]

    # Evolve the population
    g = 0
    best_in_each_generation = [] # best solution in each iteration
    global_best = []
    while g < ngen:
        print(" --- Generation %i ----" % g)
        # select the net generation individual
        offspring = toolbox.select(pop, len(pop))
        # Clone the selected individuals
        offspring = list(map(toolbox.clone, offspring))

        # next is to apply crossover and mutation on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < crossover_rate:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < mutation_rate:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        pop[:] = offspring    
        # Gather all the fitnesses in one list and print the stats
        fits = [ind.fitness.values[0] for ind in pop]
        
        # print results summary in each iteration
        # length = len(pop)
        # mean = sum(fits) / length
        # sum2 = sum(x*x for x in fits)
        # std = abs(sum2 / length - mean**2)**0.5
        # print("  Min %s" % min(fits))
        # print("  Max %s" % max(fits))
        # print("  Avg %s" % mean)
        # print("  Std %s" % std)

        # store the best solution in each iteration
        best_in_each_generation.append(tools.selBest(pop, 1)[0])
        if g == 0:
            # in the first generation, set global best solution
            global_best.append(tools.selBest(pop, 1)[0])
        else:
            # in the following generations, 
            # compare the global best with the best solution obtained in the generation
            # if the newly generated solution is better, then update the global best
            if tools.selBest(pop, 1)[0].fitness.values[0] < global_best[-1].fitness.values[0]:
                global_best.append(tools.selBest(pop, 1)[0])
            else:
                # if not updated, then the global best does not change and equal to the one in previous generation
                global_best.append(global_best[-1])
        g = g + 1
    print("-- End of (successful) evolution --")
    # decode the best solution value
    fre = decode(global_best[-1],nbit_per_var,nvars,lb,ub)
    print("Best individual is %s, fre is %s, obj is %s" % (global_best[-1], fre,global_best[-1].fitness.values))
    # plot convergence curve
    x = []
    y = []
    for i in range(0, len(global_best)):
        x.append(i)
        y.append(global_best[i].fitness.values)
    plt.plot(x,y,'bo',x,y,'k')
    plt.ylabel('Fitness Value')
    plt.xlabel('No. of Generations')
    plt.show()


def decode(chrom,nbit,nvar,lb,ub):
    
    """
    reference: Haupt, R. L., & Haupt, S. E. (2004). Practical genetic algorithms. John Wiley & Sons.
    at the end of this reference book, you can find similar matlab code
        convert binary representations to float variables
        nbit: number of bits for a one decision variable
        nvar: number of variables
        chrom: individual chromosome 
        nbit*nvar = length of chromosome  
        lb: lower bound of the decsion variables
        ub: ub bound of the decision variables
    """
    quant = []
    for i in range(0,nbit):
        quant.append(math.pow(0.5,i+1))
    sum_quant = sum(quant)
    for i in range(0, len(quant)):
        quant[i] = quant[i]/sum_quant
    float_var = [] # decoded float decision variables
    for i in range(0, nvar):
        val = 0
        for j in range(0, nbit):
            val += quant[j]*chrom[i*nbit+j]            
        float_var.append(val*(ub[i]-lb[i])+lb[i])
     
    return float_var


if __name__ == "__main__":
    main()

