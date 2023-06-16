
from abc import abstractmethod

import numpy as np

from ga.problem import Problem
from ga.individual import Individual

class IntVectorIndividual(Individual):

    def __init__(self, problem: Problem, num_genes: int):#criaçao do vetor de inteiros
        super().__init__(problem, num_genes)
        self.genome = np.full(num_genes, 0, dtype=int)#preenche os restantes com 0´s
        # TODO



    def swap_genes(self, other, index: int):
        aux = self.genome[index]
        self.genome[index] = other.genome[index]
        other.genome[index] = aux

    @abstractmethod
    def compute_fitness(self) -> float:
        pass

    @abstractmethod
    def better_than(self, other: "IntVectorIndividual") -> bool:
        pass
