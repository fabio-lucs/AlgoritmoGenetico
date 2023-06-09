def dynamicProgramming(V, P, maxCap, n):
    K = [[0] * (maxCap + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for cap in range(maxCap + 1):
            if i == 0 or cap == 0:
                K[i][cap] = 0
            elif P[i - 1] <= cap:
                K[i][cap] = max(V[i - 1] + K[i - 1][cap - P[i - 1]], K[i - 1][cap])
            else:
                K[i][cap] = K[i - 1][cap]

    return K[n][maxCap]


# Valores e pesos dos itens
V = [15, 90, 50, 60, 12]
P = [10, 40, 26, 32, 8]

# Capacidade máxima da mochila e número total de itens
maxCap = 60
n = len(V)

# Chamada da função dynamicProgramming()
resultado = dynamicProgramming(V, P, maxCap, n)

# Exibição do resultado
print("O valor máximo que pode ser alcançado é:", resultado)