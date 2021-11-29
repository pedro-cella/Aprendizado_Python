print("====== DESAFIO 25 ======")
print("""Sobre o programa: Crie um programa que leia o nome de uma pessoa
e diga se ela tem "SILVA" no nome""")
nome = input("Insira um nome: ")
nome = nome.upper()
silva = "SILVA" in nome
print("O nome {} possui SILVA: {}".format(nome, silva))