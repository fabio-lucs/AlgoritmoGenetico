import time


class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


def knapsack_greedy(items, capacity):
    sorted_items = sorted(items, key=lambda x: x.value / x.weight, reverse=True)
    final_solution = []
    total_weight = 0
    total_value = 0
    for item in sorted_items:
        if item.weight <= capacity:
            final_solution.append(item)
            capacity -= item.weight
            total_weight += item.weight
            total_value += item.value
    return final_solution, total_weight, total_value


items = [
    # Exemplo com 5 itens
    Item(10, 15),  # Item 1: peso = 10, valor = 15
    Item(40, 90),  # Item 2: peso = 40, valor = 90
    Item(26, 50),  # Item 3: peso = 26, valor = 50
    Item(32, 60),  # Item 4: peso = 32, valor = 60
    Item(8, 12),  # Item 5: peso = 8, valor = 12
]


capacity = 60
start_time = time.time()
solution, total_weight, total_value = knapsack_greedy(items, capacity)

print("Itens selecionados para a mochila:")
for item in solution:
    print("Peso:", item.weight, "| Valor:", item.value)

print("Soma dos pesos dos itens escolhidos:", total_weight)
print("Peso total:", capacity)
print("Soma dos valores dos itens escolhidos:", total_value)

end_time = time.time()
execution_time = end_time - start_time
print(f"Tempo de execução: {execution_time} segundos")
