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
        # TODO : Checar se isso está bom (Renato)
        pass

    def compute_fitness(self) -> float:
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

                # calcula a distancia
                distance = abs(current_position[0] - previous_position[0]) + \
                           abs(current_position[1] - previous_position[1])
                agent_distance += distance # atualiza a distancia percorrida pelo agente

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

    def obtain_all_path(self):
        # Inicializa as variáveis para rastrear a distância total e o total de colisões
        # TODO

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
        new_instance.total_distance = self.total_distance
        new_instance.total_collisions = self.total_collisions
        return new_instance

