from sklearn import adjusted_mutual_info_score

def ami(particao1, particao2):
    return adjusted_mutual_info_score(particao1, particao2)