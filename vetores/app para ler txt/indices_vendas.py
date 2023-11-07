import csv
import numpy as np

# Leitura dos dados do arquivo CSV e armazenamento em vetores
nomes = []
total_vendas = []
comissoes = []

with open('dados_vendas.csv', mode='r') as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)
    for linha in leitor:
        nomes.append(linha['Nome'])
        total_vendas.append(float(linha['Total_Vendas']))
        comissoes.append(float(linha['Comissao']))

# Conversão das listas em vetores numpy
total_vendas = np.array(total_vendas)
comissoes = np.array(comissoes)

# Encontrar os 2 funcionários que mais venderam usando argsort
indices_mais_venderam = np.argsort(total_vendas)[::-1][:2]
funcionarios_mais_venderam = [(nomes[i], total_vendas[i]) for i in indices_mais_venderam]

# Encontrar os 2 funcionários com menor comissão usando argsort
indices_menor_comissao = np.argsort(comissoes)[:2]
funcionarios_menor_comissao = [(nomes[i], comissoes[i]) for i in indices_menor_comissao]

# Exibir os resultados
print("Os 2 funcionários que mais venderam:")
for nome, total_vendas in funcionarios_mais_venderam:
    print(f"{nome} - Total de Vendas: {total_vendas}")

print("\nOs 2 funcionários com menor comissão:")
for nome, comissao in funcionarios_menor_comissao:
    print(f"{nome} - Comissão: {comissao}")
