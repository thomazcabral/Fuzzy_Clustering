import numpy as np
from sklearn.metrics import pairwise_distances
from sklearn.metrics import adjusted_rand_score

def medoids_init(X, k):
    total_distances = np.sum(pairwise_distances(X), axis=1) # soma das distâncias de cada ponto para todos os outros pontos
    medoid_indices = np.argsort(total_distances)[:k] # índices dos k pontos com as menores somas de distância
    medoids = X[medoid_indices] # seleciona os medoides com base nos índices
    return medoids


def assign_labels(X, medoids): 
    distances = pairwise_distances(X, medoids) # calcula a distância de cada ponto para cada medoide
    labels = np.argmin(distances, axis=1) # seleciona o índice do medoide mais próximo para cada ponto
    return labels


def swap_medoids(X, medoids, labels):
    while True:
        improved = False # se não mudar nenhum medoide, o loop é interrompido
        for i, medoid in enumerate(medoids):  # para cada medoide
            cluster = X[labels == i] # seleciona os pontos do cluster atual
            old_distance = np.sum(pairwise_distances(cluster, medoid.reshape(1, -1))) # distância total do medoide atual para os pontos do cluster

            for point in cluster:
                new_medoid = point # substitui o medoide atual por um ponto do cluster para analisar se a distância total diminui
                new_distance = np.sum(pairwise_distances(cluster, new_medoid.reshape(1, -1))) # distância total do novo medoide para os pontos do cluster
                if new_distance < old_distance:  # se a troca reduz a distância total
                    medoids[i] = new_medoid # substitui o medoide
                    labels = assign_labels(X, medoids)  # reatribui os pontos aos clusters
                    old_distance = new_distance # atualiza a distância total
                    improved = True  # indica que uma melhoria foi encontrada para não encerrar o loop
    
        if not improved:  # sai do loop se nenhuma melhoria foi encontrada
            break
    
    return medoids, labels


def adjusted_rand_index(true_labels, pred_labels):
    return adjusted_rand_score(true_labels, pred_labels)


def experimento_monte_carlo(X, true_labels, k, num_trials):
    ari_values = [] # lista para armazenar os valores do índice Rand ajustado
    
    for i in range(num_trials):
        initial_medoids = medoids_init(X, k) # inicializa os medoides
        initial_allocation = assign_labels(X, initial_medoids) # atribui os pontos aos clusters
        final_medoids, pred_labels = swap_medoids(X, initial_medoids, initial_allocation) # otimiza os medoides e as alocações
        ari = adjusted_rand_index(true_labels, pred_labels) # calcula o índice Rand ajustado
        ari_values.append(ari) # armazena o índice Rand ajustado
    
    mean_ari = np.mean(ari_values) # média dos índices Rand ajustados
    std_ari = np.std(ari_values) # desvio padrão dos índices Rand ajustados
    
    return mean_ari, std_ari


X = np.array([
    [1.0, 2.0], [1.5, 2.5], [1.2, 1.8],  # Cluster 0
    [2.0, 3.0], [2.5, 2.7], [2.3, 3.2],  # Cluster 0 (overlapping with cluster 1)
    [3.5, 3.5], [4.0, 4.0], [3.8, 3.8],  # Cluster 1
    [5.0, 5.0], [5.5, 5.2], [4.9, 5.1],   # Cluster 1 (but overlapping with cluster 2)
    [7.0, 8.0], [7.5, 7.8], [6.8, 8.1],  # Cluster 2
])

true_labels = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2])

k = 3
num_trials = 100
mean_ari, std_ari = experimento_monte_carlo(X, true_labels, k, num_trials)

print(f"Monte Carlo k-medoids Clustering Results ({num_trials} trials)")
print(f"Mean Rand Index: {mean_ari:.4f}")
print(f"Standard Deviation of Rand Index: {std_ari:.4f}")