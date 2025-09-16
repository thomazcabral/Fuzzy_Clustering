library(dplyr)
library(ppclust)
library(e1071)
library(aricode)

df <- read.csv('Iris.csv')

df <- df %>%
  select(-Id) %>%
  mutate(Species = case_when(
    Species == "Iris-setosa" ~ 0,
    Species == "Iris-versicolor" ~ 1,
    Species == "Iris-virginica" ~ 2
  ))

colnames(df) <- c("SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Class")

labels <- df$Class
df_dados <- df %>% select(-Class)
dados <- as.matrix(df_dados)

simulacao_monte_carlo <- function(dados, labels, num_clusters, num_trials) {
  indices_rand <- numeric(num_trials)
  indices_ami <- numeric(num_trials)
  
  for (i in 1:num_trials) {
    res.gk <- ppclust::gk(x = dados, centers = num_clusters, m = 2.0, dmetric = "mahalanobis")
    predicted_labels <- res.gk$cluster - 1
    
    ari <- e1071::classAgreement(table(labels, predicted_labels))$crand
    indices_rand[i] <- ari

    ami <- aricode::AMI(labels, predicted_labels)
    indices_ami[i] <- ami
  }
  
  media_indice_rand <- mean(indices_rand)
  dp_indice_rand <- sd(indices_rand)
  
  media_indice_ami <- mean(indices_ami)
  dp_indice_ami <- sd(indices_ami)
  
  return(list(
    media_ari = media_indice_rand,
    dp_ari = dp_indice_rand,
    media_ami = media_indice_ami,
    dp_ami = dp_indice_ami
  ))
}

num_clusters <- 3
num_trials <- 100

set.seed(123)
resultados_simulacao <- simulacao_monte_carlo(dados, labels, num_clusters, num_trials)

cat(sprintf("Monte Carlo GK Clustering Results (%d trials)\n\n", num_trials))

cat("--- Adjusted Rand Index (ARI) ---\n")
cat(sprintf("Mean: %.4f\n", resultados_simulacao$media_ari)) # 0.718
cat(sprintf("Standard Deviation: %.4f\n\n", resultados_simulacao$dp_ari)) # 0

cat("--- Adjusted Mutual Information (AMI) ---\n")
cat(sprintf("Mean: %.4f\n", resultados_simulacao$media_ami)) # 0.749
cat(sprintf("Standard Deviation: %.4f\n", resultados_simulacao$dp_ami)) # 0