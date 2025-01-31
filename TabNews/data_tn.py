# %%

import json
import os
from pyspark.sql import SparkSession

# %%

spark = (SparkSession.builder.appName("Python Spark SQL basic example")
                             .config("spark.some.config.option", "some-value")
                             .getOrCreate())

# %%

json_dir = "C:/yourdirectory/coleta_dados/TabNews/json/"
files = [os.path.join(json_dir, f) for f in os.listdir(json_dir) if f.endswith(".json")]
df = spark.read.json(files)
df.show()

# %%
