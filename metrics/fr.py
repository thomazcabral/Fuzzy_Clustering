def pertinence_distance(delta_k, delta_k_linha, c):
    # calcula a distância entre δ_k e δ_k' (matrizes de pertinência)
    return (1/c) * np.sum((delta_k - delta_k_linha) ** 2)

def fuzzy_rand_index(particao1, particao2, c):
    n = particao1.shape[0]
    total_sum = 0

    for k in range(n):
        for k_linha in range(k+1, n):
            if k != k_linha:
                # calcula a métrica para P
                delta_k = particao1[k]
                delta_k_prime = particao1[k_linha]
                EP = 1 - pertinence_distance(delta_k, delta_k_prime, c)

                # calcula a métrica para Q
                delta_k_Q = particao2[k]
                delta_k_prime_Q = particao2[k_linha]
                EQ = 1 - pertinence_distance(delta_k_Q, delta_k_prime_Q, c)

                total_sum += np.abs(EP - EQ) # soma a diferença absoluta entre EP e EQ

    denominador = n * (n - 1) / 2
    if denominador == 0:
        raise ValueError

    return 1- (total_sum / denominador)
