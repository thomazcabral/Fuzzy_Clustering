library(MASS)
library(dplyr)
library(ppclust)
library(e1071)
library(aricode)

simulacao_monte_carlo_gk <- function(dados, labels, num_clusters, num_trials) {
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
  
  return(list(
    media_ari = mean(indices_rand),
    dp_ari = sd(indices_rand),
    media_ami = mean(indices_ami),
    dp_ami = sd(indices_ami),
    raw_ari = indices_rand,
    raw_ami = indices_ami
  ))
}

df_completo <- read.csv("dados_sinteticos_python.csv")
lista_dfs <- split(df_completo, df_completo$config)
set.seed(123)
num_trials <- 100
resultados_finais <- list()

for (i in 1:length(lista_dfs)) {
  df_atual <- lista_dfs[[i]]
  
  cat(sprintf("\nProcessando Configuração %d...\n", i))
  
  labels_atuais <- df_atual$class
  dados_atuais <- df_atual %>% select(x1, x2) %>% as.matrix()
  
  num_clusters_atual <- length(unique(labels_atuais))
  resultados_sim <- simulacao_monte_carlo_gk(dados_atuais, labels_atuais, num_clusters_atual, num_trials)
  
  resultados_finais[[i]] <- data.frame(
    Configuracao = i,
    Media_ARI = resultados_sim$media_ari,
    DP_ARI = resultados_sim$dp_ari,
    Media_AMI = resultados_sim$media_ami,
    DP_AMI = resultados_sim$dp_ami
  )
  
  print(paste("Média ARI:", round(resultados_sim$media_ari, 4)))
  print(paste("DP ARI:", round(resultados_sim$dp_ari, 4)))
  print(paste("Média AMI:", round(resultados_sim$media_ami, 4)))
  print(paste("DP AMI:", round(resultados_sim$dp_ami, 4)))
  
  ari_string <- paste(round(resultados_sim$raw_ari, 4), collapse = ", ")
  cat(sprintf("Lista ARI (formato Python): [%s]\n", ari_string))
  
  ami_string <- paste(round(resultados_sim$raw_ami, 4), collapse = ", ")
  cat(sprintf("Lista AMI (formato Python): [%s]\n", ami_string))
}

df_resultados <- bind_rows(resultados_finais)

cat("\n--- RESULTADOS FINAIS DA SIMULAÇÃO (SEM PADRONIZAÇÃO) ---\n")
print(df_resultados)
