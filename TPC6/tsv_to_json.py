import pandas as pd
import json

# Carregar title.basics.tsv
print("Carregando title.basics.tsv...")
colunas = ["tconst", "originalTitle", "startYear", "runtimeMinutes", "genres"]
df = pd.read_csv("title.basics.tsv", sep="\t", usecols=colunas, dtype=str, na_values="\\N")
df = df.dropna().head(500)
print("Title.basics carregado. Primeiras linhas:")
print(df.head())

# Carregar title.akas.tsv
print("\nCarregando title.akas.tsv...")
akas_colunas = ["titleId", "language", "region"]
df_akas = pd.read_csv("title.akas.tsv", sep="\t", usecols=akas_colunas, dtype=str, na_values="\\N")
print("Title.akas carregado. Primeiras linhas:")
print(df_akas.head())

# Juntar ao df original
df = df.merge(df_akas, left_on="tconst", right_on="titleId", how="left").drop(columns=["titleId"])
print("\nApós merge com title.akas:")
print(df.head())

# Carregar title.principals.tsv
print("\nCarregando title.principals.tsv...")
principals_colunas = ["tconst", "nconst", "category"]
df_principals = pd.read_csv("title.principals.tsv", sep="\t", usecols=principals_colunas, dtype=str, na_values="\\N")
df_principals = df_principals[df_principals["category"].isin(["actor", "writer", "producer"])]
print("Title.principals carregado. Primeiras linhas:")
print(df_principals.head())

# Juntar ao df original
df = df.merge(df_principals, on="tconst", how="left")
print("\nApós merge com title.principals:")
print(df.head())

# Carregar name.basics.tsv
print("\nCarregando name.basics.tsv...")
names_colunas = ["nconst", "primaryName"]
df_names = pd.read_csv("name.basics.tsv", sep="\t", usecols=names_colunas, dtype=str, na_values="\\N")
print("Name.basics carregado. Primeiras linhas:")
print(df_names.head())

# Juntar os nomes
df = df.merge(df_names, on="nconst", how="left")
print("\nApós merge com name.basics:")
print(df.head())

# Criar JSON de filmes
print("\nCriando JSON de filmes...")
filmes_json = (
    df.groupby(["tconst", "originalTitle", "startYear", "runtimeMinutes", "genres", "language", "region"])
    .agg({"nconst": lambda x: list(x.dropna().unique())})
    .reset_index()
    .to_dict(orient="records")
)
print("JSON de filmes criado. Exemplo:")
print(json.dumps(filmes_json[:2], indent=4, ensure_ascii=False))

# Criar JSON de pessoas
print("\nCriando JSON de pessoas...")
pessoas_json = (
    df[["nconst", "category", "primaryName"]]
    .drop_duplicates()
    .dropna()
    .to_dict(orient="records")
)
print("JSON de pessoas criado. Exemplo:")
print(json.dumps(pessoas_json[:2], indent=4, ensure_ascii=False))

# Guardar os JSONs
with open("filmes.json", "w", encoding="utf-8") as f:
    json.dump(filmes_json, f, indent=4, ensure_ascii=False)

with open("pessoas.json", "w", encoding="utf-8") as f:
    json.dump(pessoas_json, f, indent=4, ensure_ascii=False)

print("\nJSONs gerados com sucesso!")
