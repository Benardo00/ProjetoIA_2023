import math as mt
import numpy as np
from agentsearch.heuristic import Heuristic
from warehouse.warehouse_problemforSearch import WarehouseProblemSearch
from warehouse.warehouse_state import WarehouseState


class HeuristicWarehouse(Heuristic[WarehouseProblemSearch, WarehouseState]):

    def __init__(self):
        super().__init__()
        self._goal_matrix_positions = None

    def compute(self, state: WarehouseState) -> float:#foi implementado
        # TODO
        h = 0
        h1 = 0
        h2 = 0
        for i in range(state.rows):
            for j in range(state.columns):
                tile = state.matrix[i][j]
                # Blank is ignored so that the heuristic is admissible
                if tile != 0:
                    tile_goal_line, tile_goal_column = self._goal_matrix_positions[tile]
                    h1 = abs(i - tile_goal_line)
                    h2 = abs(j - tile_goal_column) #calcula a ditancia entre os 2 pontos
                    h = mt.sqrt(h1**2+h2**2); #calcula a distancia euclidiana
        return h

    @property
    def problem(self):
        return self._problem

    @problem.setter
    def problem(self, problem: WarehouseProblemSearch):
        self._problem = problem
        self.build_aux_arrays()

    def __str__(self):
        return "Tiles distance to final position"
            # TODO
    #---foi adicionado

    def build_aux_arrays(self) -> None:
        goal_matrix = self._problem.goal_state.matrix
        goal_matrix_positions = []
        for i in range(9):
            position = np.where(goal_matrix == i)
            goal_matrix_positions.append(position)
        self._goal_matrix_positions = np.array(goal_matrix_positions)



