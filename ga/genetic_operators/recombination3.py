import random

from ga.genetic_operators.recombination import Recombination
from ga.individual import Individual

class Recombination3(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:#Two-Point Crossover (TPX)
        # TODO
        size = len(ind1.genome)
        pontoParaOCrossover1 = random.randint(0, size - 1) #selecionar os pontos aleatoriamente
        pontoParaOCrossover2 = random.randint(0, size - 1)

        point1, point2 = min(pontoParaOCrossover1, pontoParaOCrossover2), max(pontoParaOCrossover1, pontoParaOCrossover2) #o ponto1 tem que ser menor

        ind1.genome = ind1.genome[:point1] + ind2.genome[point1:point2] + ind1.genome[point2:]
        ind2.genome = ind2.genome[:point1] + ind1.genome[point1:point2] + ind2.genome[point2:]


    def __str__(self):
        return "Recombination 3 (" + f'{self.probability}' + ")"