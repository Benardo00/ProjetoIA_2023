class Pair:
    def __init__(self, cell1, cell2, value, solution):
        self.cell1 = cell1
        self.cell2 = cell2
        self.value = value
        #self.pair_path = []
        self.solution = solution
        # self.pair_path adicionar


        #guardar a lista de celulas correspondentes aquele troço

        #print(self.value)
        # TODO

        #temos que pecorrer os pares e usar o A*
        #agente e destino
        #temos que alterar o valor para aparecer na gui quando se faz run




    def hash(self):
        return str(self.cell1.line) + "_" + str(self.cell1.column) + "_" + str(
            self.cell2.line) + "_" + str(self.cell2.column)

    def __str__(self):
        return str(self.cell1.line) + "-" + str(self.cell1.column) + " / " + str(self.cell2.line) + "-" + str(self.cell2.column) + ": " + str(self.value) + "\n"

