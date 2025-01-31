# %%

import requests
import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm
import matplotlib.pyplot as plt

# %%

# Read data from a Parquet file
df_new = pd.read_parquet("dados_re.parquet")
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df_new

# %%

# Swap values in the specified row
df_new.at[101, 'Ano de nascimento'], df_new.at[101, 'de nascimento'] = df_new.at[101, 'de nascimento'], df_new.at[101, 'Ano de nascimento']
print(df_new.loc[101])

# %%

# Drop the 'de nascimento' column
df_drop = df_new.drop(columns=['de nascimento'])

# %%

# Function to replace certain values
def replace_values(value):
    if isinstance(value, list) or isinstance(value, pd.Series):
        return value.apply(replace_values)
    elif isinstance(value, str):
        if value in ["desconhecido", "desconhecido."]:
            return "Desconhecido."
        elif value in ["desconhecida", "desconhecida."]:
            return "Desconhecida."
        return value

columns_to_transform = df_drop.columns.difference(["Aparicoes"])
df_drop[columns_to_transform] = df_drop[columns_to_transform].applymap(replace_values)

# %%

df_drop['Ano de nascimento'] = df_drop['Ano de nascimento'].fillna('Desconhecido.')  # Fill NaN with 'Desconhecido.' for 'Ano de nascimento'
df_drop['Tipo sanguíneo'] = df_drop['Tipo sanguíneo'].fillna('Desconhecido.')  # Fill NaN with 'Desconhecido.' for 'Tipo sanguíneo'
df_drop['Altura'] = df_drop['Altura'].fillna('Desconhecida.')  # Fill NaN with 'Desconhecida.' for 'Altura'
df_drop['Peso'] = df_drop['Peso'].fillna('Desconhecido.')  # Fill NaN with 'Desconhecido.' for 'Peso'
df_drop['Ano de nascimento'] = df_drop['Ano de nascimento'].str.replace(r'\s?\(.*\)', '', regex=True) # Remove text in parentheses from 'Ano de nascimento'
df_drop['Altura'] = df_drop['Altura'].astype(str) # Ensure that the values in the 'Altura' column are strings
df_drop['Altura'] = df_drop['Altura'].str.replace(r'cm', 'm', regex=True) # Replace 'cm' with 'm'
df_drop = df_drop.rename(columns={'Aparicoes': 'Aparições'}) # Rename 'Aparicoes' column to 'Aparições'
df_drop.loc[139, 'Ano de nascimento'] = df_drop.loc[139, 'Ano de nascimento'].capitalize() # Capitalize the value of 'Ano de nascimento'

# %%

# Set the value of 'Ano de nascimento' to 'Desconhecido'
df_drop.loc[115, 'Ano de nascimento'] = 'Desconhecido.'
df_drop.loc[91, 'Ano de nascimento'] = 'Desconhecido.'
df_drop.loc[15, 'Ano de nascimento'] = 'Desconhecido.'

# %%

df_drop.to_csv("re_details.csv", index=False) # Save the DataFrame to a CSV file without the index
df_drop.to_parquet("re_details.parquet", index=False) # Save the DataFrame to a Parquet file without the index

# %%

