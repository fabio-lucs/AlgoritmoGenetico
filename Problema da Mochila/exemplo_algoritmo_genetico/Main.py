import time
import random

start_time = time.time()

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


def genetic_algorithm(
    items, max_weight, population_size, num_generations, mutation_rate
):
    population = create_population(population_size, len(items))

    for generation in range(num_generations):
        population = sorted(
            population, key=lambda x: fitness(x, items, max_weight), reverse=True
        )

        # Elitism: keep the best individual from the previous generation
        new_population = [population[0]]

        while len(new_population) < population_size:
            parent1 = random.choice(population[: population_size // 2])
            parent2 = random.choice(population[: population_size // 2])
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population

    best_individual = max(population, key=lambda x: fitness(x, items, max_weight))
    best_fitness = fitness(best_individual, items, max_weight)

    return best_individual, best_fitness


items = [
    Item(10, 15),  # Item 1: weight = 10, value = 15
    Item(40, 90),  # Item 2: weight = 40, value = 90
    Item(26, 50),  # Item 3: weight = 26, value = 50
    Item(32, 60),  # Item 4: weight = 32, value = 60
    Item(8, 12),  # Item 5: weight = 8, value = 12
]

max_weight = 60
population_size = 50
num_generations = 100
mutation_rate = 0.1

best_individual, best_fitness = genetic_algorithm(
    items, max_weight, population_size, num_generations, mutation_rate
)

print("Best solution:", best_individual)
print("Best fitness:", best_fitness)

# Calculate the total weight and total value of the best solution
total_weight = 0
total_value = 0
for i in range(len(best_individual)):
    if best_individual[i] == 1:
        total_weight += items[i].weight
        total_value += items[i].value

print("Total weight of the solution:", total_weight)
print("Total value of the solution:", total_value)

end_time = time.time()
execution_time = end_time - start_time
print(f"Tempo de execução: {execution_time} segundos")
