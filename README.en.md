🇧🇷 [Leia em Português](README.md)

# Multivariate Fuzzy C-Medoids (MFCMd)

This study addresses the multivariate fuzzy clustering method using medoids, whose central objective is to reduce the influence of outliers in the formation of clusters. The repository's intent is to share implementations of these methodologies, allowing for analysis and experimentation with different fuzzy clustering techniques.
#### **Student: Thomaz Cabral Corrêa de Araújo**
Lattes: http://lattes.cnpq.br/4354434691905652
#### **Advisor: Dr. Renata Maria Cardoso Rodrigues**
Lattes: http://lattes.cnpq.br/9289080285504453

## 🏆 Award-winning work

This project was awarded at the **29th Undergraduate Research Journey of FACEPE** (Foundation for the Support of Science and Technology of the State of Pernambuco), in the area of Exact Sciences, for the work:

**"Multivariate fuzzy clustering method using medoids"**

Developed at UFPE - Recife, under the supervision of Dr. Renata Maria Cardoso Rodrigues de Souza, presented in June 2025.

![Certificado FACEPE](certificadoFACEPE.jpg)

Presentation at the 29th Undergraduate Research Journey of Facepe: [slides](https://www.canva.com/design/DAGo61Ga6N4/L8GUuXTosJLe99xlXGjVQg/view?utm_content=DAGo61Ga6N4&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=hcf5310cd39)

New project for 2025/26, proposing the addition of weights to the distances and membership degrees in the proposed method (MFCMd):

### Abstract
This research project aims to advance the state-of-the-art of partition-based clustering techniques through the development of basic research on multivariate fuzzy clustering methods based on medoids and weighted distances. These distances allow for improving the quality of the obtained clustering by considering groups of different shapes and sizes. The study will address the incorporation of multivariate membership degrees, considering different dissimilarity measures with and without weights. Furthermore, an experimental evaluation with synthetic and real data will be conducted, comparing the proposed method with traditional fuzzy clustering approaches based on medoids that do not consider multivariate influence in the presence of outliers.

### Introduction
Cluster analysis is one of the main tools in data mining, with applications ranging from consumer segmentation to the classification of biological species. Among the various existing approaches, fuzzy partitioning methods stand out for their ability to model the ambiguity inherent in many real datasets, where the boundaries between groups are not always well-defined. The fuzzy paradigm, introduced by Bezdek [3], revolutionized the field by allowing objects to belong to multiple clusters simultaneously, with different degrees of membership.

Methods based on medoids [2] emerged as a robust alternative to traditional techniques that use centroids calculated by averaging. While approaches like Fuzzy C-Means are sensitive to outliers, medoids—actual representatives of the data—offer greater stability in situations with noise or extreme values. This characteristic makes methods like Fuzzy C-Medoids useful in practical applications where data quality cannot be guaranteed a priori.

Recently, the incorporation of multivariate aspects into membership degrees has opened new possibilities for the interpretation of clusters [4]. Unlike traditional methods that assign a single membership degree per object, multivariate approaches allow for analyzing how each individual variable contributes to the formation of clusters. This additional granularity enables deeper insights into the data structure, revealing, for example, that certain features may be more relevant for some groups than for others.

The use of weighted distances in this context represents a natural advancement, as it recognizes that different attributes may have distinct importance in the clustering process. While conventional methods treat all variables as equally relevant, adaptive weighting allows the algorithm itself to discover and emphasize the most discriminative features for each specific cluster. Recent works [5] have already demonstrated the effectiveness of this approach in multivariate methods based on means, showing significant gains in clustering quality. This capability is valuable in complex datasets, where the relevance of variables can vary significantly between different groups, and becomes even more crucial when combined with the robustness of medoids.

### Objective
The main objective of this work is to develop an innovative multivariate fuzzy clustering method based on medoids, capable of determining optimal weights for each variable in different clusters. The proposed method will integrate these weights into both the medoid selection process and the calculation of membership degrees, allowing the relevance of each attribute to be dynamically adjusted according to the data structure. Additionally, it seeks to create a robust approach that maintains effectiveness even in the presence of outliers and noisy variables. Finally, it is intended that the developed technique not only improves the accuracy of the clusters but also offers greater interpretability by revealing which variables are most discriminative in each group.

In this context, the intent of this work is to answer two research questions (hypotheses):

1. Does the combined use of medoids and multivariate weighting result in greater robustness against outliers, preserving the cluster structure even in datasets with high noise levels?
2. Does the incorporation of adaptive weights in the calculation of multivariate distances significantly improve the quality of the clusters when compared to methods that use fixed weights or do not consider the differential importance of variables.

### Methodology
To develop and validate the proposed method, the work will follow an experimental approach divided into four main stages.

In the first stage, a comprehensive bibliographic review will be conducted on fuzzy clustering methods, with an emphasis on techniques based on medoids and approaches that use variable weighting. This review will serve as the basis for the mathematical formalization of the new method, which will combine multivariate membership degrees with a dynamic weighting scheme updated iteratively during the clustering process.

The second stage will consist of the computational implementation of the algorithm, using the Python language. The method will follow a structure similar to multivariate Fuzzy C-Locs, but with the inclusion of an additional step for calculating the weights of the variables in each cluster. These weights will be adjusted based on the dispersion within the groups, so that variables with lower variance within a cluster receive greater weight, reinforcing their importance in defining that specific group.

The third stage will focus on experimental evaluation, using synthetic data. Sets with different levels of noise, outliers, and correlations between variables will be generated, allowing the method's robustness to be tested in controlled scenarios. The evaluation will be based on metrics such as the Adjusted Rand Index and the Fuzzy Rand Index, comparing the results with established methods [1]. Furthermore, a sensitivity analysis via Monte Carlo simulation will be conducted, with 100 replications for each scenario, to ensure the statistical stability of the results.

Finally, the fourth stage will apply the method to real datasets, allowing the practical utility of the approach in real-world problems to be verified. The interpretation of the estimated weights will be a central point, as it will provide information about which variables were most relevant for the formation of each cluster, adding a layer of interpretability to the results. By the end of the study, the proposed method is expected to demonstrate superiority over traditional techniques, especially in scenarios with heterogeneous data or aberrant data, while also offering a valuable tool for exploring patterns in complex multivariate data.

### Refererences
[1] Jain, A. K., Murty, M. N., & Flynn, P. J. (1999). Data clustering: a review. ACM computing
surveys (CSUR), 31(3), 264-323.

[2] Kaufman, L. (1987) Clustering by means of medoids. In: Proc. Statistical Data Analysis Based
on the L1 Norm Conference, Neuchatel. [S.l.: s.n.],. p. 405–416.

[3] PEIZHUANG, W. (1983) Pattern Recognition with Fuzzy Objective Function Algorithms (James
C. Bezdek). SIAM Review, v. 25, n. 3, p. 442–442.

[4] Pimentel, B.A. e Souza, R.M.C.R. (2013). A Multivariate Fuzzy C-Means Method. Applied Soft
Computing (Print). Applied Soft Computing, v.13, p.1592 - 1607.

[5] Pimentel, B. A.e Souza, R.M.C.R. (2015) Multivariate Fuzzy C-Means algorithms with
weighting. Neurocomputing, v. 174, p. 946–965.
