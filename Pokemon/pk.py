# %%

import requests
import datetime
import json
import os
import pandas as pd
from pyspark.sql import Window
from pyspark.sql.functions import col, explode, row_number
from pyspark.sql import SparkSession
from multiprocessing import Pool

# %%

class Collector:
    
    def __init__(self, url):
        self.url = url
        self.instance = url.strip("/").split("/")[-1]
    
    # Method to make GET request with any given parameters
    def get_endpoint(self, **kwargs):
        resp = requests.get(self.url, params=kwargs)
        return resp
    
    # Method to save API response data to a JSON file with timestamp
    def save_data(self, data):
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S.%f")
        data["ingestion_date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        filename = f"C:/Users/babilun/Desktop/coleta_dados/Pokemon/{self.instance}/{now}.json"
        with open(filename, "w") as openfile:
            json.dump(data, openfile)
            
    def get_and_save(self, **kwargs):
        resp = self.get_endpoint(**kwargs)
        if resp.status_code == 200: # Check if response is successful
            data = resp.json()
            self.save_data(data) # Save the data to file
            return data
        else:
            return{}
    
    # Method to collect data in paginated form from the API until no more data is available
    def auto_exec(self, limit=100):
        offset = 0
        while True:
            print(offset)
            data = self.get_and_save(limit=limit, offset=offset)
            
            if data["next"] == None:
                break
            
            offset += limit

# %%

url = "https://pokeapi.co/api/v2/pokemon"
collector = Collector(url)
collector.auto_exec() # Start the automatic collection process

# %%

# Create a Spark session for working with Spark DataFrames
spark = (SparkSession.builder.appName("Python Spark SQL basic example")
                             .config("spark.some.config.option", "some-value")
                             .getOrCreate())

# %%

json_dir = "C:/Users/babilun/Desktop/coleta_dados/Pokemon/pokemon/"
files = [os.path.join(json_dir, f) for f in os.listdir(json_dir) if f.endswith(".json")]
df = spark.read.json(files)
df.show()

# %%

# Explode the "results" column into individual Pokémon rows
exploded_df = df.withColumn("pokemon", explode(col("results")))
exploded_df.show(truncate=False)

# %%

# Select specific columns and rename them (your second block remains unchanged)
pokemon_df = exploded_df.select(
    col("ingestion_date"),
    col("pokemon.name").alias("pokemon_name"),
    col("pokemon.url").alias("url")
)
pokemon_df.show(truncate=False)

# Define a window specification to partition by Pokémon name and order by ingestion_date descending
window_spec = Window.partitionBy("pokemon_name").orderBy(col("ingestion_date").desc())

# Add a row number column based on the window specification
ranked_df = pokemon_df.withColumn("row_number", row_number().over(window_spec))

# Filter to keep only the rows where row_number == 1 (last occurrence for each Pokémon)
latest_pokemon_df = ranked_df.filter(col("row_number") == 1).drop("row_number")
latest_pokemon_df.show(truncate=False)

# %%

path = "C:/Users/babilun/Desktop/coleta_dados/Pokemon/pokemon_list/pokemon_list.csv"

# Convert the PySpark DataFrame to a Pandas DataFrame and save it as a CSV file
poke_pd = latest_pokemon_df.toPandas()
poke_pd.to_csv(path, index=False)