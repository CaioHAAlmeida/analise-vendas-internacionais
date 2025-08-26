# Importando as bibliotecas

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Importando os arquivos

arquivo = r"C:\Users\caioh\OneDrive\Portifólio\Projetos\Projeto 1\data.csv"
df = pd.read_csv(arquivo, encoding="latin1")


# Renomeando as colunas

novos_nomes = {
    "InvoiceNo": "id_pedido",
    "StockCode": "id_produto",
    "Description": "nome_produto",
    "Quantity": "quantidade",
    "InvoiceDate": "data",
    "UnitPrice": "preco_unitario",
    "CustomerID": "id_cliente",
    "Country": "pais"
}

df = df.rename(columns=novos_nomes)







# Formatando os tipos de coluna

df['id_pedido'] = df['id_pedido'].astype("string")
df['id_produto'] = df['id_produto'].astype("string")
df['nome_produto'] = df['nome_produto'].astype("string")
df['pais'] = df['pais'].astype('string')
df['quantidade'] = pd.to_numeric(
    df['quantidade'], errors='coerce').astype('Int64')
df['data'] = pd.to_datetime(
    df["data"], errors='coerce', infer_datetime_format=True)
df["preco_unitario"] = pd.to_numeric(
    df["preco_unitario"].astype(str).str.replace(".", "", regex=False).str.replace(",", ".", regex=False),
    errors="coerce"
)

df["id_cliente"] = df["id_cliente"].fillna("cliente_desconhecido").astype(str)







# Criar coluna para identificar se é compra ou devolução
df["tipo_transacao"] = df["quantidade"].apply(
    lambda x: "Devolução" if x < 0 else "Compra")







# Verificando valores ausentes antes do tratamento

nulos_pre = (
    df.isna().sum()
      .rename("n_nulos")
      .to_frame()
      .assign(pct_nulos=lambda x: (x["n_nulos"]/len(df)*100).round(2))
      .reset_index()
      .rename(columns={"index": "coluna"})
)
print("\nNulos pré tratamento:")
print(nulos_pre)
print('Quantidade de linhas:', len(df))


# Aplicando o tratamento de valores ausentes

# Excluindo linhas nulas de nome_produto
df = df.dropna(subset=["nome_produto"])

# Substituir valores nulos de id_cliente por uma variável genérica
df["id_cliente"] = df["id_cliente"].fillna("cliente_desconhecido")


# Verificação dos valores nulos após o tratamento

nulos_pos = (
    df.isna().sum()
      .rename("n_nulos")
      .to_frame()
      .assign(pct_nulos=lambda x: (x["n_nulos"]/len(df)*100).round(2))
      .reset_index()
      .rename(columns={"index": "coluna"})
)
print("\nNulos após tratamento:")
print(nulos_pos)
print('Quantidade de linhas:', len(df))









# Converter para datetime completo (data + hora)
df["data"] = pd.to_datetime(
    df["data"], errors="coerce", infer_datetime_format=True)

# Criar coluna apenas com a data
df["data_pura"] = df["data"].dt.date

# Criar coluna apenas com o horário
df["hora"] = df["data"].dt.time

# Excluir a coluna original com data e hora juntos
df = df.drop(columns=["data"])








# Flag de duplicata pela regra
chave = ["id_cliente", "data_pura", "id_produto", "quantidade"]
df["is_duplicata_regra"] = df.duplicated(subset=chave, keep="first")

# Excluir todas as duplicatas (manter apenas os registros únicos)
df = df[df["is_duplicata_regra"] == False].drop(columns=["is_duplicata_regra"])








# Função para calcular limites pelo IQR
def detectar_outliers_iqr(df, coluna):
    Q1 = df[coluna].quantile(0.25)
    Q3 = df[coluna].quantile(0.75)
    IQR = Q3 - Q1
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR

    outliers = df[(df[coluna] < limite_inferior) |
                  (df[coluna] > limite_superior)]

    print(f"Coluna: {coluna}")
    print(
        f"Limite inferior: {limite_inferior:.2f}, Limite superior: {limite_superior:.2f}")
    print(f"Quantidade de outliers: {len(outliers)}\n")

    return outliers


# Detectar outliers em quantidade e preço
outliers_qtd = detectar_outliers_iqr(df, "quantidade")
outliers_preco = detectar_outliers_iqr(df, "preco_unitario")


# Criação de BoxSplots para análise de outliers

# Quantidade
plt.figure(figsize=(10, 4))
sns.boxplot(x=df["quantidade"])
plt.title("Boxplot - Quantidade (Geral)")
plt.show()

plt.figure(figsize=(10, 4))
sns.boxplot(x=df["quantidade"])
plt.xlim(0, 200)  # zoom até 200 unidades
plt.title("Boxplot - Quantidade (até 200)")
plt.show()

# Preço Unitário
plt.figure(figsize=(10, 4))
sns.boxplot(x=df["preco_unitario"])
plt.title("Boxplot - Preço Unitário (Geral)")
plt.show()

plt.figure(figsize=(10, 4))
sns.boxplot(x=df["preco_unitario"])
plt.xlim(0, 50)  # zoom até R$ 50
plt.title("Boxplot - Preço Unitário (até 50)")
plt.show()


# Antes de filtrar
print("Tamanho original:", df.shape)

# Remover outliers de quantidade
df = df[(df["quantidade"] >= -60000) & (df["quantidade"] <= 60000)]

# Remover outliers de preço unitário
df = df[(df["preco_unitario"] > 0) & (df["preco_unitario"] <= 20000)]

# Depois de filtrar
print("Tamanho após tratamento:", df.shape)


# Estatísticas descritivas básicas
tabela_stats = df[["quantidade", "preco_unitario"]].describe()

print(tabela_stats)


# Exportar para CSV
df.to_csv("dados_tratados.csv", index=False, encoding="utf-8-sig")

print("Arquivo 'dados_tratados.csv' exportado com sucesso!")
