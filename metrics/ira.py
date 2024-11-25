from sklearn.metrics import adjusted_rand_score

def indice_rand(labels, predicted_labels):
    return adjusted_rand_score(labels, predicted_labels)
