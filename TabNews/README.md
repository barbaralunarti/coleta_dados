## 🌎📊 **Tab News Data Collection**

Este projeto tem como objetivo a coleta e análise de dados do Tab News, um site de notícias colaborativas. Utilizando a API pública do Tab News, os dados são extraídos em formato JSON, salvos em diretórios apropriados e posteriormente processados com PySpark para análise.

### 🚀 **Estrutura do Projeto**

```diff  
TabNews/
├── json/           # Armazena os arquivos JSON coletados
├── parquet/        # Armazena os arquivos Parquet dos dados coletados
├── 01_basic_content.py # Script para coletar dados da API
└── 02_data_tn.py # Script para processar os dados com PySpark
```  

### 🐍 **Scripts**

### 📌 1. Coleta de Dados

O primeiro script realiza a coleta de dados da API pública do Tab News. Ele consulta a API para obter conteúdos recentes, paginando através das páginas disponíveis e salvando os dados em dois formatos: JSON e Parquet. O script continua a fazer requisições até atingir um limite de dados ou até alcançar um ponto de parada de data (em janeiro de 2020).

### 📌 2. Processamento de Dados com PySpark

O segundo script lê os arquivos JSON salvos, utilizando o PySpark, e os carrega em um DataFrame.

### 🛠 **Requisitos**

- Python **3.13.1**  
- Bibliotecas:  
  - `requests == 2.32.3`  
  - `pandas == 2.2.3`  
  - `pyspark == 3.5.4`  
