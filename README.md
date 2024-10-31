# PIBIC - Programa Institucional de Bolsas de Iniciação Científica

Este repositório reúne trabalhos sobre técnicas de agrupamento difuso multivariado, com foco em métodos que utilizam diferentes abordagens para a definição das distâncias entre elementos e seus respectivos clusters. Um dos trabalhos o método de agrupamento difuso multivariado com base na distância de City Block, explorando como esta métrica específica pode impactar a forma como as partições são calculadas. O outro estudo aborda o método de agrupamento difuso multivariado utilizando medoids, que tem como objetivo central reduzir a influência de outliers na formação dos clusters. O intuito do repositório é compartilhar implementações dessas metodologias, permitindo a análise e experimentação com diferentes técnicas de agrupamento difuso.
#### Alunos:
- **Kleberson de Araújo Bezerra**
- **Thomaz Cabral Corrêa de Araújo**

#### Orientadora: **Profa. Dra Renata Maria Cardoso Rodrigues**

## Métodos de Agrupamento Difuso Multivariado usando Distância de City Block
#### **Aluno: Kleberson de Araújo Bezerra**
Lattes: http://lattes.cnpq.br/4354434691905652
#### **Orientadora: Profa. Dra Renata Maria Cardoso Rodrigues**
Lattes: http://lattes.cnpq.br/9289080285504453

### Introdução e Justificativa
Este projeto de pesquisa tem como objetivo avançar o estado da arte das técnicas de agrupamento do tipo partitivo, por meio do desenvolvimento de pesquisa básica sobre métodos de agrupamento no paradigma difuso, com base em vetores de medianas e graus de pertinência multivariados. Serão consideradas distâncias ponderadas e não ponderadas para refinar o processo de agrupamento. Além disso, será realizada uma avaliação experimental com dados sintéticos e reais. Os métodos propostos serão comparados com técnicas tradicionais de agrupamento difuso baseadas em medianas, que não levam em conta os graus de pertinência multivariados na presença de dados aberrantes.

### Objetivo
Este trabalho propõe um método de agrupamento difuso utilizando a distância City Block (norma L1), onde os graus de pertinência de cada objeto a um determinado grupo são representados por um vetor p-dimensional, onde p é o número de variáveis. Isso permite calcular a similaridade de um objeto em relação a um protótipo com base em cada variável. A proposta é fornecer uma maior quantidade de informações para o algoritmo difuso, visando melhorar a qualidade dos agrupamentos em comparação com métodos tradicionais que não utilizam graus de pertinência multivariados. O estudo busca responder a duas principais perguntas de pesquisa: (1) É possível melhorar a qualidade dos agrupamentos difusos utilizando a distância City Block em conjunto com graus de pertinência calculados para cada variável? (2) É possível descrever a relevância de cada variável para cada grupo utilizando esses graus?

### Metodologia
Os métodos de agrupamento do tipo partitivo geram uma única partição dos dados, em vez de uma série de partições encadeadas. A determinação do número de grupos desejados pode ser desafiadora, especialmente na ausência de informações prévias suficientes sobre o conjunto de dados. Métodos particionais se dividem em duas principais categorias: rígidos e difusos. Nos métodos rígidos, os objetos pertencem a exatamente um grupo, com grau de pertinência no conjunto {0, 1}, sendo 1 quando o objeto pertence ao grupo e 0 caso contrário. O método mais popular dessa categoria é o K-Means. Já nos métodos difusos, os objetos possuem graus de pertinência para todos os grupos, variando no intervalo [0,1]. O método difuso baseado na distância City Block, amplamente utilizado na literatura, tem a vantagem de ser menos sensível a outliers ou ruídos. No entanto, não oferece uma forma de analisar quais variáveis foram mais importantes para definir o grau de pertinência final.
Neste projeto, propomos calcular o grau de pertinência multivariado para cada objeto em relação a cada variável individualmente, o que traz duas vantagens: (1) a possibilidade de interpretar a pertinência de um objeto a um grupo em função de cada variável e (2) a obtenção de mais informações dos dados, resultando em uma maior qualidade de agrupamento. As etapas do estudo incluem: (1) Implementação de um ambiente experimental para avaliar a abordagem proposta com dados artificiais, (2) Avaliação do desempenho dos métodos utilizando o índice corrigido de Rand (medida da proximidade entre uma partição a priori e a obtida pelo método) e a taxa de erro de classificação, (3) Validação com dados reais, utilizando conjuntos de dados intervalares de repositórios de Machine Learning e outros conjuntos relevantes. As medidas serão estimadas pelo método Monte Carlo, com 100 replicações para cada conjunto. Finalmente, será realizado um estudo comparativo entre o método proposto e o método tradicional de agrupamento baseado na distância City Block que não utiliza graus de pertinência multivariados. Os métodos serão implementados em Python.

### Habilidades Adquiridas
Desenvolvimento de algoritmos de agrupamento no contexto da inteligência computacional.

### Referências
[1] Bezdek, J. C. (1981). Pattern Recognition with Fuzzy Objective Function Algorithms. Plenum Press, New York. [2] Pimentel, B.A. e Souza, R.M.C.R. (2013). A Multivariate Fuzzy C-Means Method. Applied Soft Computing (Print). Applied Soft Computing, v.13, p.1592 - 1607. [3] Jajuga, Krzysztof (1991) L1-norm based fuzzy clustering. Fuzzy Sets and Systems 39 (1991) 43-50. [4] Jain, A. K., Murty, M. N., & Flynn, P. J. (1999). Data clustering: a review. ACM computing surveys (CSUR), 31(3), 264-323. [5] Jain, A. K. (2010). Data clustering: 50 years beyond K-means. Pattern Recognition Letters, 31(8), 651-666.

## Método de Agrupamento Difuso Multivariado usando Medoids

#### **Aluno: Thomaz Cabral Corrêa de Araújo**
Lattes: http://lattes.cnpq.br/4354434691905652
#### **Orientadora: Profa. Dra Renata Maria Cardoso Rodrigues**
Lattes: http://lattes.cnpq.br/9289080285504453

### Resumo
Este projeto de pesquisa visa realizar avanços no estado da arte de técnicas de agrupamento tipo partição através do desenvolvimento de pesquisas básica sobre método de agrupamento do paradigma difuso baseado em medoids e grau de pertinência multivariado. Distâncias com pesos e sem pesos também serão consideradas no método de agrupamento. Além disso, uma avaliação experimental com dados sintéticos e reais será realizada. Os métodos serão comparados com métodos de agrupamento tipo partição difuso da literatura baseado em medoids que não consideram graus de pertinência multivariado na presença de dados aberrantes.

### Introdução
Análise de Agrupamentos pode ser compreendido como uma técnica estatística que em que dado um conjunto de dados, se busca reunir em um mesmo grupo observações que possuam um maior grau de similaridade, enquanto que observações que não possuam um alto grau de dissimilaridade são alocadas em grupos distintos. Dois grupos distintos de técnicas de partição podem ser considerados: rígido e difuso [1] [2].  

O método difuso c-médias é o método de agrupamento difuso mais conhecido e geralmente possui bons resultados na abordagem difusa, além de possuir uma relativa facilidade na implementação do algoritmo. Uma desvantagem desse método é o fato dele não possuir bom desempenho quando o conjunto de dados possui dados aberrantes (outliers).  

Existem métodos difuso que não utilizam médias para o cálculo dos protótipos, como é o caso do c-medoids. É um método bastante similar ao c-médias, porém, ao invés da utilização da média, uma observação do próprio conjunto de dados minimiza a distância desse ponto para os demais do grupo, conhecida como medoid [3] [4]. Ou seja, a principal diferença perante o difuso c-médias é encontrada na lista de formação dos centróides. Nesse caso, o método c-medoids permite usar diferentes distâncias e assim pode ser menos sensível na presença de dados aberrantes ou ruídos.  

Em [5] foi introduzido o primeiro método difuso usando um grau de pertinência associado a cada variável. Esse método é uma versão do tradicional método difuso c-médias [5] para graus de pertinência multivariado. Quanto à esta abordagem difusa multivariada, algumas vantagens são perceptíveis, como por exemplo, interpretar a relevância de cada observação para um determinado grupo de acordo com cada variável, a capacidade de obter mais informação dos conjuntos de dados ajudando a melhorar a qualidade dos agrupamentos e, por último, uma nova alternativa de agrupamentos utilizando o contexto multivariado. Uma desvantagem do método proposto em [5] é o seu baixo desempenho em conjuntos com presença de dados aberrantes (outliers ou ruídos), uma vez que usa a distância Euclidiana.  

### Objetivo
Este trabalho visa apresentar um método de agrupamento difuso em que os valores do grau de pertinência das observações para cada grupo são influenciados pelas variáveis. Ou seja, o nível de similaridade de uma observação com o protótipo é dado de acordo com cada variável do conjunto de dados. O uso dessa técnica multivariada objetiva a melhora na qualidade dos agrupamentos comparado com outros já existentes na literatura que não usam grau de pertinência multivariado. É importante destacar que o método estudado será avaliado na presença de dados aberrantes ou ruído e diferentes distâncias podem ser usadas.  

Nesse contexto, o intuito desse trabalho é responder duas perguntas (hipóteses) de pesquisa:  

1. É possível melhorar a qualidade de agrupamento difuso baseado em medoids através da utilização de graus de pertinência cujos valores são calculados segundo cada variável?  
2. É possível descrever a relevância de cada variável para cada grupo usando tais graus?

### Metodologia a ser empregada
Os algoritmos de agrupamento, tipo partição, obtêm uma única partição de dados em vez de uma série encadeada de partições. A escolha do número de grupos desejados pode ser um problema, já que nem sempre existe informações a priori suficientes do conjunto de dados para definir este número. Métodos particionais podem ser classificados em duas principais categorias: rígido ou difuso [1][2]. Na primeira categoria, objetos pertencem a exatamente um grupo, onde o grau de pertinência de um objeto para um grupo pode estar no conjunto {0, 1}: 1 se o objeto pertencer ao grupo ou 0 caso contrário. Um dos métodos particionais rígido mais popular é o k-médias. Na segunda categoria de métodos particionais, os objetos têm graus de pertinência para todos os grupos, onde podem estar no intervalo [0,1]. O método difuso c-médias é popularmente usado em aplicações do mundo real. Esse método é a versão do k-médias em que os objetos podem pertencer a todos os grupos com graus de pertinência assumindo valores no intervalo [0,1].  

O método que será investigado nesse trabalho é uma extensão do método PAM (Partition Around Medoids) [3][4]. Este algoritmo possui como principal contraste perante o k-médias a escolha de observações do conjunto de dados para serem os centróides, denominados de medoids. Neste formato, há uma maior facilidade na interpretabilidade dos centróides dos clusters perante o k-médias que utiliza a média das observações dos grupos para capturar os centróides.  

Nesse contexto, este trabalho objetiva propor uma versão difusa para o método PAM considerando graus de pertinência multivariado para cada indivíduo/objeto do conjunto de dados. A ideia é melhorar a qualidade do agrupamento usando graus de pertinência definidos por indivíduo, grupo e variável conforme o trabalho descrito em [5]. Além disso, uma versão com distâncias ponderadas também será proposta e os métodos serão avaliados na presença de outliers (pontos aberrantes). Durante a investigação, serão realizadas as seguintes ações:  

1. Implementação de um ambiente experimental para avaliação das abordagens propostas com dados artificiais. O desempenho dos métodos será avaliado baseando-se no índice corrigido de Rand (medida de proximidade entre uma partição à priori e uma partição obtida pelo método de cluster) e na taxa de erro de classificação. Na validação com dados reais, serão considerados conjuntos de dados de tipo intervalo de um repositório de Machine Learning e/ou outros conjuntos pertinentes a aplicação de cunho prático.  

2. Implementação de um ambiente experimental para avaliação das abordagens propostas com conjuntos de dados artificiais. As medidas serão estimadas pelo método Monte Carlo com 100 replicações de cada conjunto.  

3. Estudo comparativo entre o método proposto com o método de agrupamento correspondente da literatura que não usa graus de pertinência multivariado. Os métodos serão implementados usando a linguagem Python.

### Principais contribuições
Este trabalho visa contribuir de três maneiras diferentes:  

1. Realizar avanços no plano teórico relativo aos métodos de agrupamento tipo partição com publicação em conferência ou revista internacional.  
2. Formação de um aluno de graduação em uma área que apresenta potencial para aplicações em tratamento de imagens, comércio eletrônico, ciências biológicas, perfil de consumidores, etc.  
3. Criação de uma aplicação de agrupamento do mundo real para formação de perfis de dados.

### Referências
1. Jain, A. K., Murty, M. N., & Flynn, P. J. (1999). Data clustering: a review. ACM computing surveys (CSUR), 31(3), 264-323.  
2. Jain, A. K. (2010). Data clustering: 50 years beyond K-means. Pattern Recognition Letters, 31(8), 651-666.  
3. Kaufman, L.; Rousseeu, P. J. Finding groups in data: An introduction to cluster analysis–john wiley & sons. Inc., New York, 1990.  
4. Kaufman, L. Clustering by means of medoids. In: Proc. Statistical Data Analysis Based on the L1 Norm Conference, Neuchatel, 1987. p. 405–416.  
5. Pimentel, B.A. e Souza, R.M.C.R. (2013). A Multivariate Fuzzy C-Means Method. Applied Soft Computing (Print). Applied Soft Computing, v.13, p.1592-1607. 
