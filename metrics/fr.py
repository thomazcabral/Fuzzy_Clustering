import numpy as np
from scipy.spatial.distance import pdist, squareform

def fuzzy_rand_index(particao1, particao2):
    n = particao1.shape[0] # número de observações

    EP = 1 - squareform(pdist(particao1, 'euclidean'))  # E_P(x,x') = 1 - ||P(x) - P(x')||
    EQ = 1 - squareform(pdist(particao2, 'euclidean'))  # E_Q(x,x') = 1 - ||Q(x) - Q(x')||

    # soma das discordâncias
    total_discordance = np.sum(np.abs(EP - EQ)) / 2  # soma para todo (x,x') ∈ C |E_P(x,x') - E_Q(x,x')|

    # normaliza pelo número de pares
    denominador = n * (n - 1) / 2
    d = total_discordance / denominador  # distância entre as partições

    return 1 - d  # valor final

particao1 = np.array([[0.5, 0.2, 0.3], [0.1, 0.8, 0.1], [1, 0, 0]])  # P
particao2 = np.array([[0.9, 0.1, 0], [0.7, 0.1, 0.2], [0.3, 0.2, 0.4]])  # Q

fri = fuzzy_rand_index(particao1, particao2)
print(f"Fuzzy Rand Index: {fri:.4f}")
