# Mini Game

# Choose two types of Pokémon and see which ones exist and their characteristics

# %%

import os
import json
import pandas as pd
import requests

# %%

folder_path = "C:/yourdirectory/coleta_dados/Pokemon/pokemon_list/poke_url/"

# %%

pokemon_data = []

# Iterating over the files in the specified folder
for file_name in os.listdir(folder_path):
    if file_name.endswith(".json"):
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as file:
            data = json.load(file)
            # Extracting the relevant information from JSON
            name = data.get('forms', [{}])[0].get('name', 'unknown')
            types = [t['type']['name'] for t in data.get('types', [])]
            height = data.get('height', 'unknown')
            weight = data.get('weight', 'unknown')
            encounters = data.get('location_area_encounters', '')
            
            # Adding the extracted data to the list
            pokemon_data.append({
                'name': name,
                'types': types,
                'height': height,
                'weight': weight,
                'encounters': encounters
            })
            
df = pd.DataFrame(pokemon_data)

# Expanding the types column so that each type has a separate row
df = df.explode('types').reset_index(drop=True)

# %%

# Listing the unique types of Pokémon
types_list = df['types'].unique().tolist()
print("Types of Pokémon: ", types_list)

# %%

# Prompting the user to choose two types of Pokémon
while True:
    type1 = input("Choose the first type of Pokémon: ").strip().lower()
    if type1 in types_list: # Checking if the first type chosen is valid
        break
    print("Invalid type. Please try again.")
    
while True:
    type2 = input("Choose the second type of Pokémon: ").strip().lower()
    if type2 in types_list: #  Checking if the second type chosen is valid
        break
    print("Invalid type. Please try again.")
    
# Filtering the DataFrame to find Pokémon that have both types chosen
filtered_pokemon = df.groupby('name').filter(lambda x: set([type1, type2]).issubset(set(x['types'])))

# Checking if any Pokémon were found with the chosen types
while filtered_pokemon.empty:
    print(f"No Pokémon were found with the types: {type1} e {type2}.")
    type2 = input("Choose another second type: ").strip().lower()
    filtered_pokemon = df.groupby('name').filter(lambda x: set([type1, type2]).issubset(set(x['types'])))

# Displaying data on found Pokémon
for _, row in filtered_pokemon.iterrows():
    print(f"\nNome: {row['name'].title()}\nAltura: {row['height']}\nPeso: {row['weight']}")
    
    # If there is a dating URL, make a request to get the locations
    if row['encounters']:
        resp = requests.get(row['encounters'])
        if resp.status_code == 200:
            locations = [loc['location_area']['name'] for loc in resp.json()]
            print("Places where it can be found: ", locations if locations else "Unknown.")
        else:
            print("Error when searching for places where it can be found.")
    else:
        print("Places where it can be found: Unknown.")
                
# %%
