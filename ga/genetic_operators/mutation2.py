import random

from ga.genetic_algorithm import GeneticAlgorithm
from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation
from ga.population import Population


class Mutation2(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    """
    population_size = len(population.individuals)
        for i in range(population_size):
            if GeneticAlgorithm.rand.random() < self.probability:
                self.mutate(population.individuals[i])
    """


    def mutate(self, ind: IntVectorIndividual)-> None:  # mutaçao swap mutation
        # TODO
        index1 = random.randint(0, len(ind.genome)-1)  # genoma começa no indice 1, foi a forma definida
        index2 = random.randint(0, len(ind.genome)-1)
        if GeneticAlgorithm.rand.random() < self.probability:
            ind.genome[index1], ind.genome[index2] = ind.genome[index2], ind.genome[index1]#confirmar





def __str__(self):
    return "Mutation 2 (" + f'{self.probability}' + ")"
