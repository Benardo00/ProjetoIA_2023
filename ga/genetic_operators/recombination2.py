import random

from ga.individual import Individual
from ga.genetic_operators.recombination import Recombination

class Recombination2(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        # TODO
        size = len(ind1.genome)
        start, end = sorted([random.randint(0, size - 1), random.randint(0, size - 1)])
        aux1 = ind1.genome[start:end + 1]
        aux1 += [gene for gene in ind2.genome if gene not in aux1]
        aux2 = ind2.genome[start:end + 1]
        aux2 += [gene for gene in ind1.genome if gene not in aux2]
        ind1.genome = aux1
        ind2.genome = aux2

    def __str__(self):
        return "Recombination 2 (" + f'{self.probability}' + ")"
