def find_medoids(self, X, U):
    medoids = np.zeros((self.c, self.p))

    for i in range(self.c):
        for j in range(self.p):
            # distância entre todos os pontos em uma única dimensão
            dists = (X[:, j][:, np.newaxis] - X[:, j][np.newaxis, :]) ** 2  # (n, n)
            weights = U[:, i, j] ** self.m  # (n,)

            # custo total de cada ponto como possível medoide (soma ponderada das distâncias para todos os outros)
            weighted_distances = np.sum(weights[:, np.newaxis] * dists, axis=0)  # (n,)
            best_idx = np.argmin(weighted_distances)
            medoids[i, j] = X[best_idx, j]  # ponto com menor custo como medoide para essa dimensão

    return medoids
