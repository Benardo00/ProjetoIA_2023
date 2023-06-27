import math as mt
import numpy as np
from agentsearch.heuristic import Heuristic
from warehouse.warehouse_problemforSearch import WarehouseProblemSearch
from warehouse.warehouse_state import WarehouseState


class HeuristicWarehouse(Heuristic[WarehouseProblemSearch, WarehouseState]):

    def __init__(self):
        super().__init__()

    def compute(self, state: WarehouseState) -> float:
        h = 0
        h1 = 0
        h2 = 0
        column = state.column_forklift
        line = state.line_forklift
        h1 = abs(column - self._problem.goal_position.column)
        h2 = abs(line - self._problem.goal_position.line) #calcula a ditancia entre os 2 pontos
        h = mt.sqrt(h1**2+h2**2); #calcula a distancia euclidiana
        return h

    @property
    def problem(self):
        return self._problem

    @problem.setter
    def problem(self, problem: WarehouseProblemSearch):
        self._problem = problem

    def __str__(self):
        return "Distance to final position"

