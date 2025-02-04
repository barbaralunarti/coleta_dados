## 🎮 **Resident Evil Data Collection and Analysis** 💢

Este projeto visa a coleta, processamento e análise de dados sobre os personagens da franquia Resident Evil. Os dados são extraídos de fontes online e armazenados em formatos como Parquet e CSV, para posterior análise e visualização. O projeto é composto por três scripts principais que lidam com diferentes aspectos dos dados.

### ✨🐍 **Scripts**

```diff  
coleta_dados/
├── ResidentEvil/
│   │   ├── 01_ResidentEvil.py  # Coleta os dados da API
│   │   ├── 02_data_details.py  # Processa e visualiza os dados
│   │   ├── 03_graficos_re.py  # Obtém detalhes dos Pokémon
│   │   ├── visualização de dados: arquivos .csv, .parquet e .png
```  

📌 1. Coleta de Dados de Personagens 🌎
   
O primeiro script coleta informações sobre personagens da franquia Resident Evil a partir do [Resident Evil Database](https://www.residentevildatabase.com/personagens/). Ele extrai informações detalhadas como nome, ano de nascimento, tipo sanguíneo, altura, peso e suas aparições nos jogos da série. O código utiliza a biblioteca `BeautifulSoup` para realizar a extração e o processamento dos dados HTML, organizando as informações coletadas em uma lista de dicionários.

📌 2. Processamento de Dados 🔍
   
O segundo script realiza o processamento dos dados obtidos. Ele lida com valores ausentes, substituindo valores desconhecidos por "Desconhecido" ou "Desconhecida", e realiza ajustes nos dados, como a remoção de texto extra de colunas e a conversão de unidades (por exemplo, convertendo altura de cm para metros). O resultado é salvo em arquivos CSV e Parquet para uso futuro.

📌 3. Análise e Visualização 📊
   
O terceiro script carrega os dados processados e realiza a análise de informações, como o número de jogos em que cada personagem aparece e a distribuição de dados completos versus desconhecidos.  
Ele gera gráficos de barras e pizza utilizando `Matplotlib` e `Seaborn`, visualizando os dados sobre os personagens, seus jogos e a qualidade das informações disponíveis. Os gráficos gerados são salvos como arquivos PNG.

### ✔️🚀 **Objetivos do Projeto**

Coletar dados detalhados sobre personagens de Resident Evil.  
Processar e limpar os dados, tratando valores ausentes e realizando ajustes necessários.  
Analisar os dados, identificando padrões e visualizando as informações de maneira intuitiva.  
Gerar relatórios e gráficos para fácil interpretação e análise.  

### 🛠 **Requisitos**

- Python **3.13.1**  
- Bibliotecas:  
  - `requests == 2.32.3`  
  - `pandas == 2.2.3`  
  - `seaborn == 0.13.2`  
  - `tqdm == 4.67.1`  
  - `numpy == 2.2.1`  
  - `bs4 == 4.12.3`  
