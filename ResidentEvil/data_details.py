# %%

import requests
import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm

# %%

df_new = pd.read_parquet("dados_re.parquet")
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df_new

# %%

df_new.at[101, 'Ano de nascimento'], df_new.at[101, 'de nascimento'] = df_new.at[101, 'de nascimento'], df_new.at[101, 'Ano de nascimento']
print(df_new.loc[101])

# %%

df_drop = df_new.drop(columns=['de nascimento'])
df_drop

# %%

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
