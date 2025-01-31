# %%

import requests
import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import random

# %%

# Read data from a Parquet file
df = pd.read_parquet("re_details.parquet")
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df

# %%

# Identificando número de jogos por personagem

# Contar o número de jogos por personagem, considerando tanto listas quanto arrays numpy
df['Num_Jogos'] = df['Aparições'].apply(lambda x: len(x) if isinstance(x, (list, np.ndarray)) else 0)

# Limitar a exibição aos 20 personagens com mais jogos
df_sorted = df.sort_values('Num_Jogos', ascending=False)
df_top_20 = df_sorted.head(20)

# %%

# Função para gerar uma cor aleatória
def random_color():
    return [random.random(), random.random(), random.random()]

# Criar o gráfico de barras
plt.figure(figsize=(20, 8))

# Criar as barras com cores diferentes
colors = [random_color() for _ in range(len(df_top_20))]
plt.bar(df_top_20['Nome'], df_top_20['Num_Jogos'], color=colors)
plt.xlabel('Personagens', fontsize=14)
plt.ylabel('Número de Jogos', fontsize=14)
plt.title('Top 20 Personagens com mais jogos em Resident Evil', fontsize=16)
plt.xticks(rotation=90, fontsize=12)
plt.tight_layout()
plt.savefig('C:/yourdirectory/coleta_dados/ResidentEvil/grafico_barras.png', dpi=300)
plt.show()

# %%

# Criar um gráfico de pizza sem os rótulos diretamente na pizza
plt.figure(figsize=(10, 10))
plt.pie(df_top_20['Num_Jogos'], autopct='%1.1f%%', colors=plt.cm.Paired.colors, labels=None)
plt.title('Top 20 Personagens com mais jogos em Resident Evil', fontsize=16)
plt.legend(df_top_20['Nome'], title="Personagens", bbox_to_anchor=(1.05, 0.5), loc='center left', fontsize=10, title_fontsize=14)
plt.tight_layout()
plt.savefig('C:/yourdirectory/coleta_dados/ResidentEvil/grafico_pizza.png', dpi=300)
plt.show()

# %%

# Identificando dados que são desconhecidos

# Função para verificar se o dado é desconhecido
def is_unknown(value):
    return value in ["Desconhecido.", "Desconhecida.", "Desconhecido"]

# Identificar os dados desconhecidos em colunas específicas
df['Ano_de_nascimento_completo'] = ~df['Ano de nascimento'].apply(is_unknown)
df['Altura_completa'] = ~df['Altura'].apply(is_unknown)
df['Peso_completo'] = ~df['Peso'].apply(is_unknown)

# Calcular a quantidade de dados completos versus desconhecidos
dados_completos = df[['Ano_de_nascimento_completo', 'Altura_completa', 'Peso_completo']].sum(axis=1)
dados_desconhecidos = 3 - dados_completos  # Como temos 3 colunas, o número de dados desconhecidos é 3 - dados completos

# Contar o número de personagens com dados completos vs desconhecidos
dados_completos_count = (dados_completos == 3).sum()
dados_desconhecidos_count = (dados_completos != 3).sum()

print(f'Número de personagens com dados completos: {dados_completos_count}')
print(f'Número de personagens com dados desconhecidos: {dados_desconhecidos_count}')

# Gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie([dados_completos_count, dados_desconhecidos_count], 
        labels=['Completos', 'Desconhecidos'], 
        autopct='%1.1f%%', 
        colors=['silver', '#F06A56'], 
        startangle=90, 
        wedgeprops={'edgecolor': 'black'})

plt.title('Distribuição de Dados Completos vs Desconhecidos', fontsize=14)
plt.tight_layout()
plt.savefig('C:/yourdirectory/coleta_dados/ResidentEvil/grafico_desconhecidos.png', dpi=300)
plt.show()

# %% 

# Visualizando número de personagens por jogo

# Expandir a lista de jogos em linhas separadas para facilitar a contagem
df_exploded = df.explode('Aparições')

# Contar o número de personagens únicos por jogo
jogos_counts = df_exploded.groupby('Aparições')['Nome'].nunique().sort_values(ascending=False)

# Gráfico de barras
plt.figure(figsize=(14, 7))
sns.barplot(x=jogos_counts.index, y=jogos_counts.values, palette="viridis")
plt.xlabel('Jogos', fontsize=14)
plt.ylabel('Número de Personagens', fontsize=14)
plt.title('Número de personagens por jogo na franquia Resident Evil', fontsize=16)
plt.xticks(rotation=90, fontsize=12, ha='right')
plt.tight_layout()
plt.savefig('C:/yourdirectory/coleta_dados/ResidentEvil/jogo_vs_personagens.png', dpi=300)
plt.show()