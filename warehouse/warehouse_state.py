import numpy as np
from PIL.ImageEnhance import Color
from numpy import ndarray

import constants
from agentsearch.state import State
from agentsearch.action import Action


class WarehouseState(State[Action]):

    def __init__(self, matrix: ndarray, rows, columns): #ter que alterar o construtor, a matriz é sempre a mesma
        super().__init__()                              #Posição do fortlift, vai definir o estado o resto é igual

        self.line_forklift = None
        self.column_forklift = None
        self.line_exit = None
        self.column_exit = None

        self.rows = rows
        self.columns = columns
        self.matrix = np.full([self.rows, self.columns], fill_value=0, dtype=int)

        for i in range(self.rows):
            for j in range(self.columns):
                self.matrix[i][j] = matrix[i][j]#percorre a mtriz para preencher algumas prpriedades adicionais
                if self.matrix[i][j] == constants.FORKLIFT:#empilhadora
                    self.line_forklift = i
                    self.column_forklift = j
                if self.matrix[i][j] == constants.EXIT:#ponto de entrega
                    self.line_exit = i
                    self.column_exit = j


    def can_move_up(self) -> bool:  #não precisamos de alterar o ques está na matriz, só precisamos de alterar a posição da empilhadora
        return self.line_forklift > 0 and self.matrix[self.line_forklift - 1][self.column_forklift] != constants.SHELF
        # Retorna True se a empilhadora não estiver na primeira linha do ambiente e se a célula acima dela não for uma prateleira.

    def can_move_right(self) -> bool:
        return self.column_forklift < self.columns - 1 and self.matrix[self.line_forklift][self.column_forklift + 1] != constants.SHELF
        # Retorna True se a empilhadora não estiver na última coluna do ambiente e se a célula à direita dela não for uma prateleira.

    def can_move_down(self) -> bool:
        return self.line_forklift < self.rows - 1 and self.matrix[self.line_forklift + 1][self.column_forklift] != constants.SHELF
        # Retorna True se a empilhadora não estiver na última linha do ambiente e se a célula abaixo dela não for uma prateleira.

    def can_move_left(self) -> bool:
        return self.column_forklift > 0 and self.matrix[self.line_forklift][self.column_forklift - 1] != constants.SHELF
        # Retorna True se a empilhadora não estiver na primeira coluna do ambiente e se a célula à esquerda dela não for uma prateleira.

    def move_up(self) -> None:
        if self.can_move_up():
            self.matrix[self.line_forklift][self.column_forklift] = self.matrix[self.line_forklift - 1][self.column_forklift]
            self.line_forklift -= 1
            self.matrix[self.line_forklift][self.column_forklift] = constants.FORKLIFT

    def move_right(self) -> None:
        if self.can_move_right():
            self.matrix[self.line_forklift][self.column_forklift] = self.matrix[self.line_forklift][self.column_forklift + 1]
            self.column_forklift += 1
            self.matrix[self.line_forklift][self.column_forklift] = constants.FORKLIFT

    def move_down(self) -> None:
        if self.can_move_down():
            self.matrix[self.line_forklift][self.column_forklift] = self.matrix[self.line_forklift + 1][self.column_forklift]
            self.line_forklift += 1
            self.matrix[self.line_forklift][self.column_forklift] = constants.FORKLIFT

    def move_left(self) -> None:
        if self.can_move_left():
            self.matrix[self.line_forklift][self.column_forklift] = self.matrix[self.line_forklift][self.column_forklift - 1]
            self.column_forklift -= 1
            self.matrix[self.line_forklift][self.column_forklift] = constants.FORKLIFT

    def get_cell_color(self, row: int, column: int) -> Color:
        if row == self.line_exit and column == self.column_exit and (
                row != self.line_forklift or column != self.column_forklift):
            return constants.COLOREXIT

        if self.matrix[row][column] == constants.PRODUCT_CATCH:
            return constants.COLORSHELFPRODUCTCATCH

        if self.matrix[row][column] == constants.PRODUCT:
            return constants.COLORSHELFPRODUCT

        switcher = {
            constants.FORKLIFT: constants.COLORFORKLIFT,
            constants.SHELF: constants.COLORSHELF,
            constants.EMPTY: constants.COLOREMPTY
        }
        return switcher.get(self.matrix[row][column], constants.COLOREMPTY)

    def __str__(self):
        matrix_string = str(self.rows) + " " + str(self.columns) + "\n"
        for row in self.matrix:
            for column in row:
                matrix_string += str(column) + " "
            matrix_string += "\n"
        return matrix_string

    def __eq__(self, other):
        if isinstance(other, WarehouseState):
            return np.array_equal(self.matrix, other.matrix)
        return NotImplemented

    def __hash__(self):
        return hash(self.matrix.tostring())
