# %%

import os
import requests
import datetime
import json
from pyspark.sql import SparkSession
from multiprocessing import Pool

# %%

# Create a Spark session for working with Spark DataFrames
spark = (SparkSession.builder.appName("Python Spark SQL basic example")
                             .config("spark.some.config.option", "some-value")
                             .getOrCreate())

# %%

path = "C:/yourdirectory/coleta_dados/Pokemon/pokemon_list/pokemon_list.csv"
poke = spark.read.csv(path, header=True, inferSchema=True)
poke.show()

# %%

# Extract distinct URLs from the DataFrame, convert them to a pandas DataFrame, and then to a list
urls = (poke.select("url")
            .distinct()
            .toPandas()["url"]
            .tolist()
)

print(urls)

# %%

# Define a function to save Pokémon data to a JSON file
def save_pokemon(data):
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S.%f")
    data["date_ingestion"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    id_value = data.get('id', 'unknown')  # Use 'unknown' if 'id' is missing
    filename = f"C:/yourdirectory/coleta_dados/Pokemon/pokemon_list/poke_url/{id_value}_{now}.json"
    try:
        with open (filename, "w") as open_file:
            json.dump(data, open_file)
        print(f"Saved file: {filename}.")
    except Exception as e:
        print(f"Error saving file: {e}.")

# Define a function to fetch Pokémon data from a URL, to process and save it
def get_save(url):
    try:
        print(f"Processing URL: {url}")
        resp = requests.get(url)
        if resp.status_code == 200:
            data = resp.json()
            print(f"Data obtained for ID {data.get('id', 'unknown')}.")
            save_pokemon(data)
        else:
            print(f"Unable to retrieve url data: {url}. Status code: {resp.status_code}.")
    except Exception as e:
        print(f"Error processing url data {url}: {e}.")

# %%

# Utilize multiprocessing to process the list of URLs concurrently with a pool of 5 worker processes
if __name__ == '__main__':
    with Pool(5) as p:
        p.map(get_save, urls)

# %%
