print("====== DESAFIO 24 ======")
print("""Sobre o programa: Crie u programa que leia o nome
de uma cidade e diga se ela comeca ou nao com o nome "SANTO" """)
cidade = input("Insira o nome de uma cidade: ")
lista = cidade.split()
print("SANTO" in lista[0].upper())