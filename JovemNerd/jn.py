# %%

import requests
import datetime
import json
import pandas as pd
import time
from pyspark.sql import SparkSession
import os

# %%

class Collector:
    
    # Inicialização para configurar a URL base da API e o nome da instância
    def __init__(self, url, instance_name):
        self.url = url  # URL da API que será utilizada para as requisições
        self.instance_name = instance_name

    # Método para realizar uma requisição GET na URL base com parâmetros opcionais
    def get_content(self, **kwargs):
        resp = requests.get(self.url, params=kwargs)
        return resp

    # Salvar os dados em formato Parquet
    def save_parquet(self, data):
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S.%f")
        df = pd.DataFrame(data)
        # Salva o DataFrame em formato Parquet no diretório
        df.to_parquet(f"{self.instance_name}/parquet/{now}.parquet", index=False)

    # Salvar os dados em formato JSON
    def save_json(self, data):
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S.%f")
        # Abre um arquivo no formato JSON e salva os dados
        with open(f"{self.instance_name}/json/{now}.json", 'w') as open_file:
            json.dump(data, open_file)

    # Método para salvar os dados no formato especificado
    def save_data(self, data, format='json'):
        if format == 'json':
            self.save_json(data)
        elif format == 'parquet':
            self.save_parquet(data)

    # Buscar dados da API e salvá-los
    def get_and_save(self, save_format='json', **kwargs):
        resp = self.get_content(**kwargs)
        if resp.status_code == 200:
            data = resp.json()
            self.save_data(data, save_format)
        else:
            data = None
            print(f"Request sem sucesso: {resp.status_code}", resp.json())
        return data

    # Método automatizado para executar a coleta de dados até atingir uma data limite
    def auto_exec(self, save_format='json', date_stop='2023-01-01'):
        page = 1 
        while True:
            print(page)
            data = self.get_and_save(save_format=save_format,
                                     page=page,
                                     per_page=1000)
            
            if data == None:
                print("Erro ao coletar os dados... aguardando.")
                time.sleep(60 * 5)  # Aguarda 5 minutos antes de tentar novamente
            else:
                date_last = pd.to_datetime(data[-1]["published_at"]).date()
                # Verifica se a data do último item é anterior à data limite
                if date_last<pd.to_datetime(date_stop).date():
                    break
                elif len(data)<1000:
                    break
                page += 1 
                time.sleep(5)  # Aguarda 5 segundos antes da próxima requisição.
                
# %%

url = "https://api.jovemnerd.com.br/wp-json/jovemnerd/v1/nerdcasts/"
collect = Collector(url, "episodios")
collect.auto_exec()

# %%

# Iniciar uma SparkSession com aplicação e configurações específicas
spark = (SparkSession.builder.appName("Python Spark SQL basic example")
                             .config("spark.some.config.option", "some-value")
                             .getOrCreate())

# %%

# Acessar diretório e ler os arquivos .json
json_dir = "C:/Users/babilun/Desktop/coleta_dados/JovemNerd/episodios/json/"
files = [os.path.join(json_dir, f) for f in os.listdir(json_dir) if f.endswith(".json")]
df = spark.read.json(files)
df.show()