"""
Esse código verifica há os medicamentos prescritos no estoque
"""
def contagem_ocorrencias(sequencia):
    contagem = {}

    for letra in sequencia:
        if letra in contagem:  # Se a letra se repetir, adiciona 1 a sua qtd
            contagem[letra] += 1
        else:
            contagem[letra] = 1
    return contagem  # Quantidade de vezes que a letra aparece

def produto_no_estoque(prescricao, armazenado):
    med_prescritos = contagem_ocorrencias(prescricao)  # Conta o número de meds prescritos
    disponiveis = contagem_ocorrencias(armazenado)  # Conta aqueles em estoque

    for medicamento, quantidade in med_prescritos.items():
        # Checa produtos prescritos. Caso o número seja maior que o estoque, False
        if medicamento not in disponiveis or disponiveis[medicamento] < quantidade:
            # Se o medicamento não estiver em estoque ou em quantidade insuficiente
            # Retornará False
            return False
    return True

prescricao = input("Digite a prescrição (ex: baab): ").strip()
estoque = input("Digite o estoque (ex: abaa): ").strip()
# Coleta de dados do usuário, o strip remove espaços em branco

if produto_no_estoque(prescricao, estoque):
    print("Prescrição VÁLIDA")
else:
    print("Prescrição INVÁLIDA:")
