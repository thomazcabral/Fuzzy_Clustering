def mfcm_run(dados, num_clusters, m=2, max_iter=1000, epsilon=1e-5):
    mfcm = MFCMedoids(c=num_clusters, X=dados, m=m)  
    U = mfcm.initialize_u()
    for _ in range(max_iter):
        medoids = mfcm.find_medoids(dados, U)
        D = mfcm.get_distances(dados, medoids)
        new_U = mfcm.update_u(D)
        if np.linalg.norm(U - new_U) < epsilon:
            break
        U = new_U
    Delta = np.sum(U, axis=2)  # Summing over the second axis (variables j)
    return medoids, U, Delta