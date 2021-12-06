print("====== DESAFIO 79 ======")
print("""Sobre o programa: Crie um programa onde o usuario possa digitar varios valores numericos e
cadastre-os em uma lista. Caso o numero ja exista la dentro, ele nao sera adicionado.
No final, serao exibidos todos os valores unicos digitados em ordem crescente.""")
numeros = []
numero = int(input("Digite um  valor: "))
numeros.append(numero)
print("Valor adicionado com sucesso...")
escolha = input("Quer continuar? [S/N]: ").upper()
while escolha != 'N':
    numero = int(input("Digite um  valor: "))
    if numero not in numeros:
        numeros.append(numero)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado! Nao vou adicionar...")   
    escolha = input("Quer continuar? [S/N]: ").upper()
print("-="*30)
print(f"Voce digitou os valores {sorted(numeros)}")