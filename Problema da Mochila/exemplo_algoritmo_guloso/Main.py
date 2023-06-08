class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

def knapsack_greedy(items, capacity):
    sorted_items = sorted(items, key=lambda x: x.value/x.weight, reverse=True)
    final_solution = []
    for item in sorted_items:
        if item.weight <= capacity:
            final_solution.append(item)
            capacity -= item.weight
    return final_solution

items = [
    Item(10, 15),   # Item 1: peso = 10, valor = 15
    Item(40, 90),   # Item 2: peso = 40, valor = 90
    Item(26, 50),   # Item 3: peso = 26, valor = 50
    Item(32, 60),   # Item 4: peso = 32, valor = 60
    Item(8, 12)     # Item 5: peso = 8, valor = 12

  
]

capacity = 60

solution = knapsack_greedy(items, capacity)

print("Itens selecionados para a mochila:")
for item in solution:
    print("Peso:", item.weight, "| Valor:", item.value)
