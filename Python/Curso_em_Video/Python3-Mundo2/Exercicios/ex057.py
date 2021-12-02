print("====== DESAFIO 57 ======")
print("""Sobre o programa: Faca um programa que leia o sexo de uma pessoa, mas so aceite
os valores 'M' ou 'F'. Caso esteja errado, peca a digitacao novamente ate ter um valor correto.""")
sexo = input('Insira o sexo(M ou F): ').upper()
while sexo != 'M' and sexo != 'F':
    print("Digite novamente!")
    sexo = input('Insira o sexo(M ou F): ').upper()
