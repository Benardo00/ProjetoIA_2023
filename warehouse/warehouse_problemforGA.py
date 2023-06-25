import numpy as np

from ga.problem import Problem
from warehouse.warehouse_agent_search import WarehouseAgentSearch
from warehouse.warehouse_individual import WarehouseIndividual


class WarehouseProblemGA(Problem):

    SIMPLE_FITNESS = 0 #foi acrescentado
    PENALTY_FITNESS = 1
    def __init__(self,agent_search: WarehouseAgentSearch ):
        #TODO deve faltar acrescentara algum parametro
        #self.index = index
        self.forklifts = agent_search.forklifts
        self.products = agent_search.products
        self.agent_search = agent_search
        self.exit = agent_search.exit
        self.pairs = self.agent_search.pairs

    def generate_individual(self) -> "WarehouseIndividual":#criar o genoma aqui
        numGenes = len(self.products) + (len(self.forklifts) - 1)
        new_individual = WarehouseIndividual(self, numGenes) #representar o genoma como um vetor de inteiros

        for i in range(numGenes):
            new_individual.genome[i] = i+1#comecar no1

        np.random.shuffle(new_individual.genome)#baralhar

        return new_individual


    def __str__(self):
        string = "# of forklifts: "
        string += f'{len(self.forklifts)}'
        string = "# of products: "
        string += f'{len(self.products)}'
        return string

