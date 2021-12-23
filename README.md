# Web Scraping

## Content

- [Web Scraping](#web-scraping)
  - [Content](#content)
  - [Brazilian Financial Indicies](#brazilian-financial-indicies)
    - [Objetivo](#objetivo)
    - [Organização](#organização)
    - [Produtos](#produtos)
  - [Fundamentus Bovespa Data](#fundamentus-bovespa-data)
    - [Objetivo](#objetivo-1)
    - [Organização](#organização-1)
    - [Produto](#produto)
  - [Ceasa Recife](#ceasa-recife)
    - [Objetivo](#objetivo-2)
    - [Organização](#organização-2)


## Brazilian Financial Indicies

### Objetivo

Montar uma base de dados com as séries de 27 índices econômicos brasileiro. 

### Organização

Este crawler foi construído com a biblioteca Selenium utilizando a linguagem python. Este é um crawler simples, com interação de login com as credeciais previamente cadastrada no site, aceitação de cookies da página e posterior seleção do país de interesse, e dos índices desejados. Para cada índice existe uma quantidade de séries temporais associadas. O crawler navega por diversas páginas até encontrar a que possui a janela de seleção da data desejada para realização do download dos dados.

**Recursos**:

- Python;
- Sellenium;
- Pandas;
- Jupyetr Notebook. 

### Produtos

Com esta base de dados foi produzido o seguinte paper:

FERNANDES, LEONARDO H. S. ; ARAUJO, FERNANDO H. A. DE ; SILVA, JOSE W. L. ; SILVA, MARIA A. R. . Insights into the predictability and similarity of COVID-19 worldwide lethality. Fractals-Complex Geometry Patterns And Scaling In Nature And Society, v. 29, p. 1-15, 2021. [DOI:http://dx.doi.org/10.1142/s0218348x21502212](http://dx.doi.org/10.1142/s0218348x21502212) 

## Fundamentus Bovespa Data

### Objetivo

Coletar dados dos relatórios financeiros de empresas (papel) listadas na Bolsa de Valores. 

### Organização

Esta spider foi construída com a biblioteca rvest1.0 utilizando a linguagem R. Esta simples spider navega até a página com as tabelas de cada papel listado na bolsa e coleta as cinco tabelas com informações dos relatórios. Em seguida é ralizada a organização destas tabelas em uma única e depois é realizada a busca de todos os papéis. Devido ao tempo de processamento, foi utilizado um algoritmo para paralelizar a coleta de informações e agilizar o processo.   

**Recursos**:

- R;
- rvest;
- httr;
- tidyverse;
- furr;
- RStudio. 

### Produto

Desenvolver um dashboard com as principais informações dos relatórios de cada empresa listada na Bolsa de valores brasileira.


## Ceasa Recife

### Objetivo

Coletar dados de produtos comercializados no Ceasa da cidade de Recife.

### Organização

Web scraping com requests e BeautifulSoup. This code get prices about the fish comerce at Ceasa Recife. 
