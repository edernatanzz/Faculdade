# Definindo vetores para representar os funcionários e suas vendas
funcionarios = ["Funcionario A", "Funcionario B", "Funcionario C", "Funcionario D"]
vendas = [1500, 2200, 1800, 1200]  # Valores em reais
comissoes = [0.1, 0.15, 0.12, 0.08]  # Taxa de comissão como fração (10% = 0.1)

# Encontrando os dois funcionários que mais venderam
vendas_ordenadas = sorted(enumerate(vendas), key=lambda x: x[1], reverse=True)
funcionarios_mais_venderam = [funcionarios[i] for i, _ in vendas_ordenadas[:2]]

# Encontrando os dois funcionários com menor comissão

comissoes_ordenadas = sorted(enumerate(comissoes), key=lambda x: x[1])
funcionarios_menor_comissao = [funcionarios[i] for i, _ in comissoes_ordenadas[:2]]

# Imprimindo os resultados
print("Os dois funcionários que mais venderam foram:", funcionarios_mais_venderam)
print("Os dois funcionários com menor comissão foram:", funcionarios_menor_comissao)
