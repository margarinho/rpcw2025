import pandas as pd

colunas = ["tconst", "originalTitle", "startYear", "runtimeMinutes", "genres"]
df = pd.read_csv("title.basics.tsv", sep="\t", usecols=colunas, dtype=str, na_values="\\N")

# Remover valores nulos e selecionar as primeiras 500 entradas
df = df.dropna().head(500)

# Exibir as primeiras linhas
print(df)

akas_colunas = ["titleId", "language", "region"]
df_akas = pd.read_csv("title.akas.tsv", sep="\t", usecols=akas_colunas, dtype=str, na_values="\\N")

# Filtrar apenas os títulos presentes no df original
df_akas_filtrado = df_akas[df_akas["titleId"].isin(df["tconst"])]

# Juntar os dados ao df original
df_final = df.merge(df_akas_filtrado, left_on="tconst", right_on="titleId", how="left")

# Exibir as primeiras linhas
print(df_final)