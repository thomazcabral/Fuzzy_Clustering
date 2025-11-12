# Multivariate Fuzzy C-Medoids (MFCMd)

Esse estudo aborda o método de agrupamento difuso multivariado utilizando medoids, que tem como objetivo central reduzir a influência de outliers na formação dos clusters. O intuito do repositório é compartilhar implementações dessas metodologias, permitindo a análise e experimentação com diferentes técnicas de agrupamento difuso.

#### **Aluno: Thomaz Cabral Corrêa de Araújo**
Lattes: http://lattes.cnpq.br/4354434691905652
#### **Orientadora: Profa. Dra Renata Maria Cardoso Rodrigues**
Lattes: http://lattes.cnpq.br/9289080285504453

## 🏆 Trabalho premiado

Este projeto foi **premiado na 29ª Jornada de Iniciação Científica da FACEPE** (Fundação de Amparo à Ciência e Tecnologia do Estado de Pernambuco), na área de Ciências Exatas, pelo trabalho:

**"Método de agrupamento difuso multivariado usando medoids"**

Desenvolvido na UFPE - Recife, sob orientação da Profa. Renata Maria Cardoso Rodrigues de Souza, apresentado em junho de 2025.

![Certificado FACEPE](certificadoFACEPE.jpg)

Apresentação na 29ª Jornada de Iniciação Científica da Facepe: [slides](https://www.canva.com/design/DAGo61Ga6N4/L8GUuXTosJLe99xlXGjVQg/view?utm_content=DAGo61Ga6N4&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=hcf5310cd39)

Novo projeto para 2025/26, propondo a adição de pesos nas distâncias e nos graus de pertinência no método proposto (MFCMd):

### Resumo
Este projeto de pesquisa visa realizar avanços no estado da arte de técnicas de agrupamento do tipo partição por meio do desenvolvimento de pesquisas básicas sobre métodos de agrupamento difuso multivariado baseados em medoids e distâncias ponderadas. Essas distâncias permitem melhorar a qualidade do agrupamento obtido considerando grupos de formas e tamanhos diferentes. O estudo abordará a incorporação de graus de pertinência multivariados, considerando diferentes medidas de dissimilaridade com e sem pesos. Além disso, uma avaliação experimental com dados sintéticos e reais será conduzida, comparando o método proposto com abordagens tradicionais de agrupamento difuso baseado em medoids que não consideram a influência multivariada na presença de outliers. 

### Introdução
A análise de agrupamento é uma das principais ferramentas da mineração de dados, com aplicações que abrangem desde a segmentação de consumidores até a classificação de espécies biológicas. Entre as diversas abordagens existentes, os métodos de partição difusos se destacam por sua capacidade de modelar a ambiguidade inerente a muitos conjuntos de dados reais, onde os limites entre grupos nem sempre são bem definidos. O paradigma difuso, introduzido por Bezdek [3], revolucionou a área ao permitir que objetos pertencessem a múltiplos clusters simultaneamente, com diferentes graus de pertinência.

Os métodos baseados em medoids [2] surgiram como uma alternativa robusta às técnicas tradicionais que utilizam centróides calculados por média. Enquanto abordagens como o Fuzzy C-Means são sensíveis a outliers, os medoids - representantes reais dos dados - oferecem maior estabilidade em situações com ruídos ou valores extremos. Essa característica torna métodos como o Fuzzy C-Medoids úteis em aplicações práticas onde a qualidade dos dados não pode ser garantida a priori.

Recentemente, a incorporação de aspectos multivariados nos graus de pertinência tem aberto novas possibilidades para a interpretação dos agrupamentos [4]. Diferentemente dos métodos tradicionais que atribuem um único grau de pertinência por objeto, as abordagens multivariadas permitem analisar como cada variável individual contribui para a formação dos clusters. Essa granularidade adicional possibilita insights mais profundos sobre a estrutura dos dados, revelando, por exemplo, que determinadas características podem ser mais relevantes para alguns grupos do que para outros.

O uso de distâncias ponderadas neste contexto representa um avanço natural, pois reconhece que diferentes atributos podem ter importâncias distintas no processo de agrupamento. Enquanto métodos convencionais tratam todas as variáveis como igualmente relevantes, a ponderação adaptativa permite que o próprio algoritmo descubra e enfatize as características mais discriminativas para cada cluster específico. Trabalhos recentes [5] já demonstraram a eficácia dessa abordagem em métodos multivariados baseados em média, mostrando ganhos significativos na qualidade do agrupamento. Essa capacidade é valiosa em conjuntos de dados complexos, onde a relevância das variáveis pode variar significativamente entre diferentes grupos, e se torna ainda mais crucial quando combinada com a robustez dos medoids. 

### Objetivo
Este trabalho tem como principal objetivo desenvolver um método inovador de agrupamento difuso multivariado baseado em medoids, capaz de determinar pesos ótimos para cada variável em diferentes clusters. O método proposto integrará esses pesos tanto no processo de seleção dos medoids quanto no cálculo dos graus de pertinência, permitindo que a relevância de cada atributo seja ajustada dinamicamente conforme a estrutura dos dados. Além disso, busca-se criar uma abordagem robusta que mantenha eficácia mesmo na presença de outliers e variáveis ruidosas. Por fim, pretende-se que a técnica desenvolvida não apenas melhore a acurácia dos agrupamentos, mas também ofereça maior interpretabilidade ao revelar quais variáveis são mais discriminativas em cada grupo.

Nesse contexto, o intuito desse trabalho é responder duas perguntas (hipóteses) de pesquisa:
1. O uso combinado de medoids e ponderação multivariada resulta em maior robustez contra outliers, preservando a estrutura dos clusters mesmo em conjuntos de dados com alto nível de ruído?
2. A incorporação de pesos adaptativos no cálculo de distâncias multivariadas melhora significativamente a qualidade dos agrupamentos quando comparada a métodos que utilizam ponderações fixas ou não consideram a importância diferenciada das variáveis.

### Metodologia a ser empregada
Para desenvolver e validar o método proposto, o trabalho seguirá uma abordagem experimental dividida em quatro etapas principais.

Na primeira etapa, será realizada uma revisão bibliográfica abrangente sobre métodos de agrupamento difuso, com ênfase em técnicas baseadas em medoids e abordagens que utilizam ponderação de variáveis. Essa revisão servirá como base para a formalização matemática do novo método, que combinará graus de pertinência multivariados com um esquema de pesos dinâmicos atualizados iterativamente durante o processo de agrupamento.

A segunda etapa consistirá na implementação computacional do algoritmo, utilizando a linguagem Python. O método seguirá uma estrutura semelhante ao Fuzzy C-Medoids multivariado, mas com a inclusão de um passo adicional para o cálculo dos pesos das variáveis em cada cluster. Esses pesos serão ajustados com base na dispersão dentro dos grupos, de modo que variáveis com menor variância dentro de um cluster recebam maior peso, reforçando sua importância na definição daquele grupo específico.

A terceira etapa focará na avaliação experimental, utilizando tanto dados sintéticos. Serão gerados conjuntos com diferentes níveis de ruído, outliers e correlações entre variáveis, permitindo testar a robustez do método em cenários controlados. A avaliação será baseada em métricas como o Índice de Rand Ajustado e o Índice de Rand Difuso, comparando os resultados com métodos estabelecidos [1]. Além disso, será conduzida uma análise de sensibilidade via simulação Monte Carlo, com 100 replicações para cada cenário, a fim de garantir a estabilidade estatística dos resultados.

Por fim, a quarta etapa aplicará o método a conjuntos de dados reais, permitindo verificar a utilidade prática da abordagem em problemas do mundo real. A interpretação dos pesos estimados será um ponto central, pois fornecerá informações sobre quais variáveis foram mais relevantes para a formação de cada cluster, adicionando uma camada de interpretabilidade aos resultados. Ao final do estudo, espera-se que o método proposto demonstre superioridade em relação às técnicas tradicionais, especialmente em cenários com dados heterogêneos ou com dados aberrantes, ao mesmo tempo em que oferece uma ferramenta valiosa para a exploração de padrões em dados multivariados complexos. 

### Referências
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
