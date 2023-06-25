import numpy as np

from ga.individual_int_vector import IntVectorIndividual


class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)
        self.fitness = 0
        self.problem = problem
        self.num_genes = num_genes
        self.total_distance = None
        self.total_collisions = None
        self.collision_penalty = 1000
        # TODO
        pass

    def compute_fitness(self) -> float:
        self.total_distance = 0
        self.total_collisions = 0  # acabou por não ser contabilizado na fitness
        self.fitness = 0
        # Loop to track the path of each forklift
        # loop para ver o caminho do agente
        genome = []
        aux = []
        for i in range(len(self.genome)):  # i e o nosso gene
            if self.genome[i] >= len(self.problem.products) + 1:  # guardar os separadores
                genome.append(aux.copy())
                aux.clear()  # limpar a lista auxiliar
            aux.append(self.genome[i])
            if i == len(self.genome) - 1:  # protecao se nao encontar nenhum separador
                genome.append(aux.copy())
                aux.clear()
                # ----feito a partir daqui
        for index, fork in enumerate(genome):  # index e o numero do agente
            if len(fork) == 0:  # protecao se o fokrlift nao tiver produtos
                # calcular a distancia do agente ate a saidaTODO, usando o index atual e o for dos pares
                for pair in self.problem.pairs:  # TODO
                    if pair.cell1 == self.problem.forklifts[index]:
                        if pair.cell2 == self.problem.exit:
                            self.total_distance += pair.solution.cost
                continue
            for i in range(len(fork)):
                if i == 0 and fork[i] >= len(self.problem.products) + 1:

                    for pair in self.problem.pairs:
                        if pair.cell1 == self.problem.forklifts[index]:

                            if len(fork) == 1:  # se o agente so tiver um separador
                                if pair.cell2 == self.problem.exit:
                                    self.total_distance += pair.solution.cost
                            else:
                                if pair.cell2 == self.problem.products[fork[i + 1] - 1]:
                                    self.total_distance += pair.solution.cost  # produtos é como se fosse uma celula

                    continue  # saltar quando o separador está na primeira posição

                product_index_inicial = fork[i]  # index do produto
                if i == len(fork) - 1:  # ultimo elemento
                    for pair in self.problem.pairs:
                        if pair.cell1 == self.problem.products[
                            product_index_inicial - 1]:  # comparar o porduto na posicao e comparar com o pair 1, para ir buscafr o custo da solução
                            if pair.cell2 == self.problem.exit:  # comparar o porduto na posicao e comparar com o pair 2, para ir bsucar o custo da solucao
                                self.total_distance += pair.solution.cost  # produtos sao celular
                    continue  # saltar quando o separador está na ultima posição
                product_index_final = fork[i + 1]  # index do produto

                if product_index_inicial > product_index_final:
                    product_index_inicial, product_index_final = product_index_final, product_index_inicial  # protecção
                for pair in self.problem.pairs:
                    if pair.cell1 == self.problem.products[
                        product_index_inicial - 1]:  # comparar o porduto na posicao e comparar com o pair 1, para ir bsucar o custo da solucao
                        if pair.cell2 == self.problem.products[
                            product_index_final - 1]:  # comparar o porduto na posicao e comparar com o pair 2, para ir bsucar o custo da solucao
                            self.total_distance += pair.solution.cost  # produtos sao celular
            # Define o fitness como a distância total percorrida
        self.fitness = self.total_distance
        print(self.fitness)
        return self.fitness, self.total_collisions
        # A fitness quando totalmente correta deve devolver2 valores:
        # -uma lista de dimensao igual ao num de fokrlifts; que contem as listas de celulas percorrididos por cada um dos forklifts nesta solução;
        # -o num maximo de cells percorridos por um dos forklifts, ou seja, a dimensao da maior lista de cell.

    def obtain_all_path(self):
        # Inicializa as variáveis para rastrear a distância total e o total de colisões
        # TODO
        # calcula os caminhos completos percorridos pelos fotklifts. Devolve um lista de células (as células percorridas por cada forklift);
        # e o numero maximo de passos
        # necessarios para percorrer todos os caminhos (i.e o numero de celulas do caminho mais longo percorrido por um forklift)
        # devolve o caminho do forklift que demora mais tempo a percorrer
        # Inicializa as variáveis para rastrear os caminhos e o número máximo de passos
        paths = []  # Lista de células percorridas por cada empilhadora
        max_steps = 0  # Número máximo de passos entre todos os caminhos
        # Percorre cada empilhadora no problema
        for forklift_index in range(self.num_genes):  # TODO corrigir
            current_position = self.problem.initial_state.get_forklift_position(
                forklift_index)  # Posição inicial da empilhadeira
            path = [current_position]  # Lista para armazenar as células percorridas pela empilhadeira
            steps = 0  # Número de passos percorridos pela empilhadeira

            # Executa os movimentos até atingir o objetivo
            while not self.problem.is_goal(current_position):
                available_actions = self.problem.get_actions(
                    current_position)  # Obtém as ações disponíveis para a empilhadora
                action = np.random.choice(available_actions)  # Escolhe uma ação aleatória
                new_position = self.problem.get_successor(current_position,
                                                          action)  # Executa a ação e atualiza a posição
                path.append(new_position)  # Adiciona a nova posição ao caminho da empilhadeira
                steps += 1
                current_position = new_position  # Atualiza a posição atual da empilhadeira
            paths.append(path)  # Adiciona o caminho da empilhadeira à lista de caminhos
            max_steps = max(max_steps, steps)  # Atualiza o número máximo de passos se necessário

        return paths, max_steps
        pass

    def __str__(self):
        string = 'Fitness: ' + f'{self.fitness}' + '\n\n'
        # string += 'Total de Passos: ' + '\n'
        # string += 'Caminho Mais Longo:' + '\n'

        if (self.total_collisions == 0):
            string += 'Total de Colisões: ' + 'Não Contabilizadas' + '\n\n'
        else:
            string += 'Total de Colisões: ' + f'{self.total_collisions}' + '\n\n'

        string += 'Genome: ' + '\n'
        string += str(self.genome) + "\n\n"

        # TODO mostar no painel quando se da run
        return string

    def better_than(self, other: "WarehouseIndividual") -> bool:
        return True if self.fitness < other.fitness else False

    # __deepcopy__ is implemented here so that all individuals share the same problem instance
    def __deepcopy__(self, memo):
        new_instance = self.__class__(self.problem, self.num_genes)
        new_instance.genome = self.genome.copy()
        new_instance.fitness = self.fitness
        new_instance.total_distance = self.total_distance  # foi adicionado
        new_instance.total_collisions = self.total_collisions  # foi adicionado
        return new_instance
