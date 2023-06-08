import time
start_time = time.time()
import random

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

def create_population(num_individuals, num_items):
    population = []
    for _ in range(num_individuals):
        individual = [random.randint(0, 1) for _ in range(num_items)]
        population.append(individual)
    return population

def fitness(individual, items, max_weight):
    total_value = 0
    total_weight = 0
    for i in range(len(individual)):
        if individual[i] == 1:
            total_value += items[i].value
            total_weight += items[i].weight
            if total_weight > max_weight:
                return 0  
    return total_value

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]  # flip the bit
    return individual

def genetic_algorithm(items, max_weight, population_size, num_generations, mutation_rate):
    population = create_population(population_size, len(items))

    for generation in range(num_generations):
        population = sorted(population, key=lambda x: fitness(x, items, max_weight), reverse=True)

        # Elitism: keep the best individual from the previous generation
        new_population = [population[0]]

        while len(new_population) < population_size:
            parent1 = random.choice(population[:population_size // 2])
            parent2 = random.choice(population[:population_size // 2])
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population

    best_individual = max(population, key=lambda x: fitness(x, items, max_weight))
    best_fitness = fitness(best_individual, items, max_weight)

    return best_individual, best_fitness

items = [
    Item(10, 15),   # Item 1: weight = 10, value = 15
    Item(40, 90),   # Item 2: weight = 40, value = 90
    Item(26, 50),   # Item 3: weight = 26, value = 50
    Item(32, 60),   # Item 4: weight = 32, value = 60
    Item(8,12)      #Item 5: weight = 8 , value = 12
]

# items = [
# Item(10, 15),   # Item 1: peso = 10, valor = 15
# Item(40, 90),   # Item 2: peso = 40, valor = 90
# Item(26, 50),   # Item 3: peso = 26, valor = 50
# Item(32, 60),   # Item 4: peso = 32, valor = 60
# Item(8, 12),    # Item 5: peso = 8, valor = 12
# Item(15, 30),   # Item 6: peso = 15, valor = 30
# Item(5, 20),    # Item 7: peso = 5, valor = 20
# Item(17, 25),   # Item 8: peso = 17, valor = 25
# Item(21, 45),   # Item 9: peso = 21, valor = 45
# Item(12, 35),   # Item 10: peso = 12, valor = 35
# ]
# 2,3,6,7,10

max_weight = 80
population_size = 50
num_generations = 100
mutation_rate = 0.1

best_individual, best_fitness = genetic_algorithm(items, max_weight, population_size, num_generations, mutation_rate)

print("Best solution:", best_individual)
print("Best fitness:", best_fitness)
end_time = time.time()
execution_time = end_time - start_time
print(f"Tempo de execução: {execution_time} segundos")