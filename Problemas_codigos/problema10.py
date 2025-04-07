import matplotlib.pyplot as plt
"""
Esse código cria um gráfico que mostra a quantidade de atendimentos por data.
É um exemplo de como a análise de dados pode ser usada para monitorar o desempenho de um negócio.
"""
# Possibilidade do usuário inserir as datas
# entrada = input("Digite as datas dos atendimentos separadas por vírgula (ex: 2024-04-01,2024-04-01,2024-04-02): ")
# datas_atendimentos = [data.strip() for data in entrada.split(',') if data.strip()]
# A condição no final garante que lista não receba datas vazias. O início lida com espaços vazios.


# Lista dos dias de atendimento
datas_atendimentos = [
    '2023-03-01', '2023-03-01', '2023-03-02',
    '2024-04-02', '2024-04-02', '2024-04-01',
    '2024-03-02', '2024-03-02', '2024-03-02', '2024-04-01'
]

# Número de datas
contagem = {}
for d in datas_atendimentos:
    contagem[d] = contagem.get(d, 0) + 1

# Ordenação de datas (mais antigo -> mais recente) e seleção para o gráfico
datas = sorted(contagem)
quantidades = [contagem[dts] for dts in datas]  ## dts usado para evitar confusão com o d acima

# Criação do visual do gráfico (nomes, quantidades...)
plt.bar(datas, quantidades, color='blue')
plt.title('Atendimentos por Dia')
plt.xlabel('Data')
plt.ylabel('Quantidade')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()
