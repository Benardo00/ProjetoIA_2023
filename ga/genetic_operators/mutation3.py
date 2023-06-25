import random

from ga.genetic_algorithm import GeneticAlgorithm
from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation

class Mutation3(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:#mutação inversion
        # TODO
            start_index = random.randint(0, len(ind.genome) - 3)
            if GeneticAlgorithm.rand.random() < self.probability:
                ind.genome[start_index:start_index + 3] = ind.genome[start_index:start_index + 3][::-1]

    def __str__(self):
        return "Mutation 3 (" + f'{self.probability}' + ")"
