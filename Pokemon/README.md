## 🔥🐉 Projeto de Coleta e Análise de Dados de Pokémon 🐉🔥

### **Descrição:**

Este projeto tem como objetivo coletar, processar e analisar dados dos Pokémon utilizando a `PokéAPI`. Ele está dividido em quatro partes principais, cada uma com um código específico para diferentes etapas do processamento dos dados. 🎮

### 📂 **Estrutura do Projeto:**

O projeto é composto por quatro scripts Python:

```diff  
coleta_dados/
├── Pokemon/
│   ├── pokemon_list/
│   │   ├── poke_url/  # JSONs com dados individuais dos Pokémon
│   │   ├── pokemon_list.csv  # Lista de Pokémon e URLs
│   │   ├── locations_pk.csv  # Locais onde os Pokémon podem ser encontrados
│   │   ├── gráficos  # Imagens geradas pelas análises
│   ├── scripts/
│   │   ├── 01_pk.py  # Coleta os dados da API
│   │   ├── 02_pokemon_data.py  # Processa e visualiza os dados
│   │   ├── 03_pk_details.py  # Obtém detalhes dos Pokémon
│   │   ├── 04_choose_pokemon.py  # Mini game interativo
```

### 🚀 **Executando os Códigos:**

📌 01_ Coleta de Dados da PokéAPI

◽️ Este primeiro código realiza a coleta automática dos dados dos Pokémon utilizando a PokéAPI. Ele:

Faz requisições paginadas à API para coletar informações sobre todos os Pokémon.  
Salva os dados brutos em arquivos JSON com timestamps.  
Utiliza o `Apache Spark` para carregar os dados coletados e organizar uma tabela com nomes e URLs dos Pokémon.  
Exporta uma lista de Pokémon para um arquivo CSV.

📌 02_ Processamento e Visualização dos Dados 📊

◽️ Este segundo código processa os dados extraídos e gera visualizações gráficas:

Lê os arquivos JSON contendo detalhes de cada Pokémon.  
Extrai informações como nome e tipos de cada um.  
Cria visualizações para analisar a distribuição dos Pokémon por tipo.  
Obtém e analisa dados sobre os locais onde os Pokémon podem ser encontrados.  
Exporta os dados para CSV e salva gráficos em formato PNG.

📌 03_ Coleta Detalhada de Dados dos Pokémon 🌏

◽️ O terceiro código aprofunda a coleta de dados:

Lê o arquivo CSV contendo a lista de Pokémon e extrai suas URLs.  
Utiliza multiprocessing para paralelizar as requisições e acelerar a coleta.  
Obtém dados detalhados de cada Pokémon e os salva em arquivos JSON com timestamps.

📌 04_ Mini Game: Descubra Pokémon por Tipo 🎮

◽️ O quarto código implementa um mini game interativo:

Permite que o usuário escolha dois tipos de Pokémon.
Filtra os Pokémon que possuem esses dois tipos.
Exibe suas características como nome, altura, peso e locais onde podem ser encontrados.

### 🚀🐍 **Tecnologias Utilizadas:**

`Python` para manipulação e análise de dados.  
`Requests` para fazer requisições à API.  
`Pandas` para processamento de dados.  
`Apache Spark` para manipulação eficiente de grandes volumes de informação.  
`Matplotlib` e `Seaborn` para geração de gráficos.  
`Multiprocessing` para acelerar a coleta de dados.  
`TQDM` para acompanhamento do progresso.  

### 🛠 **Requisitos:**

- Python **3.13.1**  
- Bibliotecas:  
  - `requests == 2.32.3`  
  - `pandas == 2.2.3`  
  - `pyspark == 3.5.4`  
  - `seaborn == 0.13.2`  
  - `tqdm == 4.67.1`

Este projeto é uma forma de aprender sobre coleta e análise de dados utilizando Python e ferramentas de visualização. Divirta-se explorando o mundo dos Pokémon! ♥️
