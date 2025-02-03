## 🎙 **Coleta de Dados do Jovem Nerd**  
Este projeto realiza a extração automatizada de dados dos Nerdcasts do Jovem Nerd, utilizando a API oficial da plataforma. O objetivo é coletar informações sobre os episódios, armazená-las em diferentes formatos (JSON e Parquet) e processá-las para análise posterior.

### **Funcionalidades do Código**  
1️⃣ Coleta de Dados da API

O código acessa a API do Jovem Nerd na URL:  
```bash  
https://api.jovemnerd.com.br/wp-json/jovemnerd/v1/nerdcasts/
```  
Faz requisições paginadas para obter todos os episódios disponíveis.

2️⃣ Armazenamento em JSON e Parquet

Os dados coletados podem ser salvos em dois formatos:  
JSON (para fácil leitura e compatibilidade com diversas ferramentas).  
Parquet (formato otimizado para análise de grandes volumes de dados).

3️⃣ Execução Automática até Data Limite

O script continua coletando os episódios até encontrar um cujo published_at seja anterior à data definida (`2023-01-01`).

4️⃣ Leitura e Processamento com Apache Spark

Após a coleta, os arquivos JSON são lidos utilizando `Apache Spark`, permitindo manipulação e análise eficiente dos dados.

🛠 Tecnologias Utilizadas  
✔️ Python 🐍  
✔️ Requests – Para realizar as requisições HTTP à API 🌐  
✔️ Pandas – Para estruturar e manipular os dados 📊  
✔️ Apache Spark – Para leitura e processamento eficiente 💡  
✔️ JSON e Parquet – Formatos para armazenamento de dados 🗂  
✔️ OS e Time – Para automação e gerenciamento de arquivos ⏳

### 📂 Estrutura do Código  
📌 1. Classe Collector  
A classe `Collector` é responsável por gerenciar a coleta e armazenamento dos dados.

`__init__()` – Configura a URL base e o nome da instância.
`get_content()` – Faz uma requisição GET para obter os dados.
`save_parquet()` – Salva os dados coletados no formato Parquet.
`save_json()` – Salva os dados no formato JSON.
`save_data()` – Escolhe o formato de salvamento (json ou parquet).
`get_and_save()` – Obtém os dados e os salva se a requisição for bem-sucedida.
`auto_exec()` – Executa a coleta de forma automática até atingir a data limite.

📌 2. Execução do Coletor  
```python  
url = "https://api.jovemnerd.com.br/wp-json/jovemnerd/v1/nerdcasts/"
collect = Collector(url, "episodios")
collect.auto_exec()
```  
Isso inicializa o coletor e começa a baixar os dados dos episódios.

📌 3. Processamento dos Dados com Spark  
Após a coleta, os arquivos JSON são carregados no Apache Spark para visualização:  
```python  
spark = (SparkSession.builder.appName("Python Spark SQL basic example")
                             .config("spark.some.config.option", "some-value")
                             .getOrCreate())

json_dir = "C:/yourdirectory/coleta_dados/JovemNerd/episodios/json/"
files = [os.path.join(json_dir, f) for f in os.listdir(json_dir) if f.endswith(".json")]

df = spark.read.json(files)
df.show()
```  
Isso permite processar os dados de forma distribuída, o que é útil para grandes volumes de informação.

### 📊 Exemplo de Saída:  
```diff  
+----------+--------------------+-------------------+
| episode  | title              | published_at      |
+----------+--------------------+-------------------+
| 685      | Nerdcast RPG: Cthulhu | 2023-12-15      |
| 684      | Tecnologia e inovação | 2023-12-08      |
| ...      | ...                | ...              |
+----------+--------------------+-------------------+
```  
Isso mostra uma amostra dos episódios coletados.

### 📌 Como Usar:  
1️⃣ Clone o repositório:

```bash  
git clone https://github.com/seu-usuario/coleta_dados.git
cd coleta_dados/JovemNerd
```

2️⃣ Instale as dependências:

```bash  
pip install requests pandas pyspark
```

3️⃣ Execute a coleta de dados:

```bash  
python script.py
```

4️⃣ Visualize os dados com Apache Spark.

### 🛠 Requisitos

- Python **3.13.1**  
- Bibliotecas:  
  - `requests == 2.32.3`  
  - `pandas == 2.2.3`  
  - `pyspark == 3.5.4`  
