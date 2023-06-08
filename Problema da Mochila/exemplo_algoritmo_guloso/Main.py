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


items = [Item(10, 60), Item(20, 100), Item(30, 120)]
capacity = 32

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
