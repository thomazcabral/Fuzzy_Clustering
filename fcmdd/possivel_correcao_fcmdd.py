def fcmdd(data, k, m=2, max_iter=1000000):
    n = data.shape[0]
    membership_matrix = init_membership_matrix(n, k)
    for _ in range(max_iter):
        medoids = update_medoids(data, membership_matrix, m)
        new_membership_matrix = atualizacao_matriz_pertinencia(data, medoids, m)
        if np.linalg.norm(new_membership_matrix - membership_matrix) < 1e-6:
            break
        membership_matrix = new_membership_matrix
    return medoids, membership_matrix