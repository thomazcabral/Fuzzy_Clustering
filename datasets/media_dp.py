import numpy as np

def simular_com_precisao(num_indices, media_desejada, dp_desejado, num_clusters):
    inicio = media_desejada - dp_desejado
    fim = media_desejada + dp_desejado
    centroides = np.linspace(start=inicio, stop=fim, num=num_clusters)
    centroides = np.maximum(0, centroides)

    print(f"Centróides gerados de forma controlada (Média: {centroides.mean():.3f}):")
    print(np.round(centroides, 3))

    repeticoes_base = num_indices // num_clusters
    resto = num_indices % num_clusters
    matriz_final = np.repeat(centroides, repeticoes_base)
    if resto > 0:
        matriz_final = np.concatenate([matriz_final, centroides[:resto]])

    np.random.shuffle(matriz_final)
    return matriz_final

MEDIA_ALVO = 0.784
DESVIO_PADRAO_ALVO = 0.007
NUM_CLUSTERS = 3
NUM_PONTOS = 100

matriz_simulada_precisa = simular_com_precisao(NUM_PONTOS, MEDIA_ALVO, DESVIO_PADRAO_ALVO, NUM_CLUSTERS)

print(f"\nMatriz simulada com alta precisão (primeiros 20):")
print(np.round(matriz_simulada_precisa[:20], 3))

print(f"Média real do resultado final: {matriz_simulada_precisa.mean():.3f} (Alvo: {MEDIA_ALVO})")
print(f"Desvio padrão real do resultado final: {matriz_simulada_precisa.std():.3f} (Alvo: {DESVIO_PADRAO_ALVO})")
