import numpy as np

def pertinence_distance(delta_k, delta_k_linha, c):
    # calcula a distância entre δ_k e δ_k' (matrizes de pertinência)
    return (1/c) * np.sum((delta_k - delta_k_linha) ** 2)

def fuzzy_rand_index(particao1, particao2):
    n = particao1.shape[0]
    c = particao1.shape[1]
    total_sum = 0
    for k in range(n):
        for k_linha in range(k+1, n):
            # calcula a métrica para P
            delta_k = particao1[k]
            delta_k_prime = particao1[k_linha]
            EP = 1 - pertinence_distance(delta_k, delta_k_prime, c)
            # calcula a métrica para Q
            delta_k_Q = particao2[k]
            delta_k_prime_Q = particao2[k_linha]
            EQ = 1 - pertinence_distance(delta_k_Q, delta_k_prime_Q, c)
            total_sum += np.abs(EP - EQ)
    denominador = n * (n - 1) / 2
    return 1 - (total_sum / denominador)

# Exemplo
particao1 = np.array([[0.5, 0.2, 0.3], [0.1, 0.8, 0.1], [1, 0, 0]])  # P
particao2 = np.array([[0.9, 0.1, 0], [0.7, 0.1, 0.2], [0.3, 0.2, 0.4]])  # Q

fri = fuzzy_rand_index(particao1, particao2)
print(f"Fuzzy Rand Index: {fri:.4f}")
