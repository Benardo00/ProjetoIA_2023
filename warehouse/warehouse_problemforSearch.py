
import copy

import constants
from agentsearch.problem import Problem
from warehouse.actions import *
from warehouse.cell import Cell
from warehouse.warehouse_state import WarehouseState


class WarehouseProblemSearch(Problem[WarehouseState]):

    def __init__(self, initial_state: WarehouseState, goal_position: Cell):
        super().__init__(initial_state)
        self.actions = [ActionDown(), ActionUp(), ActionRight(), ActionLeft()]
        self.goal_position = goal_position

    def get_actions(self, state: WarehouseState) -> list:
        valid_actions = []
        for action in self.actions:
            if action.is_valid(state):
                valid_actions.append(action)
        return valid_actions


    def get_successor(self, state: WarehouseState, action: Action) -> WarehouseState:
        successor = copy.deepcopy(state)
        action.execute(successor)
        return successor

    def is_goal(self, state: WarehouseState) -> bool:
        # TODO
        # temos que ver se o forklift está no local final e ter cuidado com as células adjacentes
        goal_position_line = self.goal_position.line
        goal_position_column = self.goal_position.column
        if self.initial_state.matrix[goal_position_line][goal_position_column] != constants.EXIT:
            if self.initial_state.matrix[goal_position_line][goal_position_column-1] == 0:#+posição verdadeira á esquerda
                goal_position_column -= 1#posição verdadeira
            else:
                goal_position_column += 1#posição verdadeira á dir
        if state.column_forklift == goal_position_column:#agora
            if state.line_forklift == goal_position_line:
                return True
            else:
                return False




