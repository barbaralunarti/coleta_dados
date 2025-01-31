# %%

import os
import json
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm

# %%

# Path to the folder containing your Pokémon JSON files
folder_path = "C:/yourdirectory/coleta_dados/Pokemon/pokemon_list/poke_url/"

# List to store the Pokémon data
pokemon_data = []

# Iterate over all JSON files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith(".json"):  # Ensure it's a JSON file
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as file:
            data = json.load(file)
            # Extract the Pokémon name
            name = data.get('forms', [{}])[0].get('name', 'unknown')
            
            # Extract the Pokémon types
            types = [t['type']['name'] for t in data.get('types', [])]
            
            # Append the data to the list
            pokemon_data.append({'name': name, 'types': types})

df = pd.DataFrame(pokemon_data)
df = df.explode('types').reset_index(drop=True)
df

# %%

# Count the number of Pokémon for each type
type_counts = df['types'].value_counts()

# %%

# Bar plot
plt.figure(figsize=(12, 6))
sns.barplot(x=type_counts.index, y=type_counts.values, palette="viridis")
plt.xlabel("Type", fontsize=14)
plt.ylabel("Number of Pokémon", fontsize=14)
plt.title("Number of Pokémon by type", fontsize=16)
plt.xticks(rotation=45, fontsize=12)
plt.tight_layout()
save_path = r"C:/yourdirectory/coleta_dados/Pokemon/pokemon_list/pokemon_types_barplot.png"
plt.savefig(save_path, dpi=300, bbox_inches='tight')
plt.show()

# %%

# Pie chart
plt.figure(figsize=(10, 8))
plt.pie(type_counts.values, autopct='%1.1f%%', startangle=140, 
        colors=plt.cm.tab20.colors)

plt.title("Distribution of Pokémon by Type", fontsize=16)
legend_labels = [f"{label}: {count}" for label, count in zip(type_counts.index, type_counts.values)]
plt.legend(legend_labels, title="Quantity", bbox_to_anchor=(1.05, 1), loc='upper left')
save_path = r"C:/yourdirectory/coleta_dados/Pokemon/pokemon_list/pokemon_types_piechart.png"
plt.savefig(save_path, dpi=300, bbox_inches='tight')
plt.show()

# %%

# List to store data
pokemon_locations = []

# Iterate over JSON files
for file_name in tqdm(os.listdir(folder_path), desc="Collecting data"):
    if file_name.endswith(".json"):  # Ensure it is JSON
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as file:
            data = json.load(file)

            # Pokémon name
            name = data.get("forms", [{}])[0].get("name", "Unknown")

            # URL for encounter locations
            encounter_url = data.get("location_area_encounters")

            # If there is the encounter location URL, make the request
            if encounter_url:
                response = requests.get(encounter_url)
                if response.status_code == 200:
                    encounters = response.json()
                    
                    # Collect the locations where Pokémon can be found
                    locations = [enc["location_area"]["name"] for enc in encounters]

                    # Add to dataset
                    pokemon_locations.append({"name": name, "locations": locations})

df_locations = pd.DataFrame(pokemon_locations)
df_locations = df_locations.explode("locations").dropna().reset_index(drop=True)

# Count how many Pokémon appear in each location
location_counts = df_locations["locations"].value_counts()

# %%

# Bar plot: Top 20 locations with the most Pokémon found
plt.figure(figsize=(12, 6))
sns.barplot(x=location_counts.head(20).index, y=location_counts.head(20).values, palette="coolwarm")
plt.xticks(rotation=90, fontsize=12)
plt.xlabel("Encounter location", fontsize=14)
plt.ylabel("Pókemon numbers", fontsize=14)
plt.title("Top 20 locations with the most Pokémon found", fontsize=16)
plt.tight_layout()
save_path = "C:/yourdirectory/coleta_dados/Pokemon/pokemon_list/pokemon_encounters_barplot.png"
plt.savefig(save_path, dpi=300, bbox_inches="tight")
plt.show()

# %%

save_path = "C:/yourdirectory/coleta_dados/Pokemon/pokemon_list/locations_pk.csv"
df_locations.to_csv(save_path, index=False)

# %%