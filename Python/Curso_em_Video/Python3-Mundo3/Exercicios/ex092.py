import datetime
print("====== DESAFIO 92 ======")
print("""Sobre o programa: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os
(com idade) em um dicionario se por acaso a CTPS for diferente de ZERO, o dicionario recebera tambem o ano de contratacao
e o salario. Calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar.""")

while True:
    nome = input("Nome: ")
    ano_nascimento = int(input("Ano de Nascimento: "))
    carteira = int(input("Carteira de Trabalho (0 nao tem): "))
    ano = datetime.datetime.now()
    idade = ano.year - ano_nascimento
    if carteira == 0:
        dicionario = {'nome': nome, 'idade': idade, 'ctps': carteira}
        break
    ano_contratacao = int(input("Ano de Contratacao: "))
    salario = float(input("Salario: R$ "))
    aposentadoria = (ano_contratacao - ano_nascimento) + 35
    dicionario = {'nome': nome, 'idade': idade, 'ctps': carteira, 'contratacao': ano_contratacao, 'salario': salario,
    'aposentadoria': aposentadoria}
    break

print("-="*30)
for k, v in dicionario.items():
    print(f"{k} tem o valor {v}")