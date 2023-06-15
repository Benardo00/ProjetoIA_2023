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

    def generate_individual(self) -> "WarehouseIndividual":#criar o genoma aqui

        new_individual = WarehouseIndividual(self, len(self.forklifts)) #representar o genoma como um vetor de inteiros
        numGenes = len(self.products) + (len(self.forklifts) - 1)
        for i in range(numGenes+1):
            new_individual.genome[i] = self.products[i]
        return new_individual

        encomendas = self.agent_search.products
        for gene in range(len(self.genome)):
            ultima_encomenda = encomendas[-1]
        forklift = ultima_encomenda + 1
        self.genome = encomendas + [forklift]



    def __str__(self):
        string = "# of forklifts: "
        string += f'{len(self.forklifts)}'
        string = "# of products: "
        string += f'{len(self.products)}'
        return string

