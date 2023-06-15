import numpy as np

from ga.individual_int_vector import IntVectorIndividual

class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)
        self.genome = []
        self.fitness = 0
        self.problem = problem
        self.num_genes = num_genes
        self.total_distance = None
        self.total_collisions = None
        self.collision_penalty = 1000
        # TODO
        pass

    def compute_fitness(self) -> float:#ver o custo do caminho inteiro
        """
        # Inicializa as variáveis para rastrear a distância total e o total de colisões
        self.total_distance = 0
        self.total_collisions = 0
        # loop para ver o caminho do agente
        for agent_path in self.genome:
            agent_position = agent_path[0] # posição inicial do agente
            agent_distance = 0 # distancia percorrida pelo agente
            agent_collisions = 0 # numero de colisões do agente
            # loop para ver o caminho do agente
            for i in range(1, len(agent_path)):
                current_position = agent_path[i] # posição atual do agente
                previous_position = agent_path[i - 1] # posição anterior do agente

                Temos que ir buscar os pares calculados anteriormente


                # verifica se o agente colidiu com outro agente
                for other_agent_path in self.genome:
                    if other_agent_path[i] == current_position:
                        agent_collisions += 1 # atualiza o numero de colisões do agente

            self.total_distance += agent_distance # atualiza a distancia total
            self.total_collisions += agent_collisions # atualiza o total de colisões

        # calcula o fitness
        fitness = self.total_distance + self.total_collisions * self.problem.collision_penalty
        # atualiza o fitness
        self.fitness = fitness

        return fitness
        """

        solution =self.pair.solution
        num_forklifts = len(solution)

        max_cells = 0
        forklift_cells = []

        for forklift in solution:
            path = []  # List to store the cells visited by the current forklift
            current_cell = forklift['start_cell']
            path.append(current_cell)

            for movement in forklift['movements']:
                if movement == 'up':
                    current_cell = (current_cell[0] - 1, current_cell[1])
                elif movement == 'down':
                    current_cell = (current_cell[0] + 1, current_cell[1])
                elif movement == 'left':
                    current_cell = (current_cell[0], current_cell[1] - 1)
                elif movement == 'right':
                    current_cell = (current_cell[0], current_cell[1] + 1)

                path.append(current_cell)

            forklift_cells.append(path)
            max_cells = max(max_cells, len(path))

        return forklift_cells, max_cells



        # devolve 2 valores:
        # -uma lista de dimensao igual ao num de fokrlifts; que contem as listas de celulas percorrididos por cada um dos forklifts nesta solução;
        # -o num maximo de cells percorridos por um dos forklifts, ou seja, a dimensao da maior lista de cell.


    def obtain_all_path(self):#podemos usar no compute fitness
        # Inicializa as variáveis para rastrear a distância total e o total de colisões
        # TODO
        # calcula os caminhos completos percorridos pelos fotklifts. Devolve um lista de células (as células percorridas por cada forklift);
        # e o numero maximo de passos
        # necessarios para percorrer todos os caminhos (i.e o numero de celulas do caminho mais longo percorrido por um forklift)
        #devolve o caminho do forklift que demora mais tempo a percorrer

        # Inicializa as variáveis para rastrear os caminhos e o número máximo de passos
        paths = []  # Lista de células percorridas por cada empilhadora
        max_steps = 0  # Número máximo de passos entre todos os caminhos

        # Percorre cada empilhadora no problema
        for forklift_index in range(self.num_genes):
            current_position = self.problem.initial_state.get_forklift_position(
                forklift_index)  # Posição inicial da empilhadeira
            path = [current_position]  # Lista para armazenar as células percorridas pela empilhadeira
            steps = 0  # Número de passos percorridos pela empilhadeira

            # Executa os movimentos até atingir o objetivo
            while not self.problem.is_goal(current_position):
                available_actions = self.problem.get_actions(current_position)  # Obtém as ações disponíveis para a empilhadora
                action = np.random.choice(available_actions)    # Escolhe uma ação aleatória
                new_position = self.problem.get_successor(current_position, action)    # Executa a ação e atualiza a posição
                path.append(new_position)  # Adiciona a nova posição ao caminho da empilhadeira
                steps += 1
                current_position = new_position  # Atualiza a posição atual da empilhadeira
            paths.append(path)  # Adiciona o caminho da empilhadeira à lista de caminhos
            max_steps = max(max_steps, steps)  # Atualiza o número máximo de passos se necessário

        return paths, max_steps
        pass

    def __str__(self):
        string = 'Fitness: ' + f'{self.fitness}' + '\n'
        string += str (self.genome) + "\n\n"
        for i in range(self.num_genes):
            string += str(self.problem.warehouse_items[i]) + "\n"
        return string

    def better_than(self, other: "WarehouseIndividual") -> bool:
        return True if self.fitness < other.fitness else False

    # __deepcopy__ is implemented here so that all individuals share the same problem instance
    def __deepcopy__(self, memo):
        new_instance = self.__class__(self.problem, self.num_genes)
        new_instance.genome = self.genome.copy()
        new_instance.fitness = self.fitness
        new_instance.total_distance = self.total_distance #foi adicionado
        new_instance.total_collisions = self.total_collisions #foi adicionado
        return new_instance

