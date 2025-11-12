import numpy as np

def simular_com_precisao(num_indices, media_desejada, dp_desejado, num_clusters):
    """
    This function generates the centroids and the final shuffled data matrix.
    It now prints the centroids as a Python list.
    """
    # Generate centroids deterministically
    inicio = media_desejada - dp_desejado
    fim = media_desejada + dp_desejado
    centroides = np.linspace(start=inicio, stop=fim, num=num_clusters)
    
    # Ensure no negative values
    centroides = np.maximum(0, centroides)

    # --- Conversion and Printing of Centroids ---
    # Convert the rounded numpy array of centroids to a Python list
    lista_centroides = np.round(centroides, 3).tolist()
    print(lista_centroides)

    # Distribute centroids to build the final matrix
    repeticoes_base = num_indices // num_clusters
    resto = num_indices % num_clusters
    matriz_final = np.repeat(centroides, repeticoes_base)
    if resto > 0:
        matriz_final = np.concatenate([matriz_final, centroides[:resto]])

    # Shuffle the final array
    np.random.shuffle(matriz_final)
    return matriz_final

# --- Parameters ---
MEDIA_ALVO = 0.273
DESVIO_PADRAO_ALVO = 0.129
NUM_CLUSTERS = 3
NUM_PONTOS = 100

# --- Execution and Final Conversion ---
# Run the simulation to get the final numpy array
matriz_simulada_np = simular_com_precisao(NUM_PONTOS, MEDIA_ALVO, DESVIO_PADRAO_ALVO, NUM_CLUSTERS)

# Convert the final rounded numpy array to a Python list
lista_simulada_final = np.round(matriz_simulada_np, 3).tolist()

# Print the final list
print(lista_simulada_final)
