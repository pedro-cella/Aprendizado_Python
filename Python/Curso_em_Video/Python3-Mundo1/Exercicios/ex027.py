print("====== DESAFIO 27 ======")
print("""Sobre o programa: Faca um programa que leia o nome complet de uma pessoa,
mostrando em seguida o primeiro e o ultimo nome separadamente.
Ex: Ana Maria de Souza
primeiro = Ana
ultimo = Souza""")
nome = input("Insira seu nome completo: ")
separa_nome = nome.split()
primeiro = separa_nome[0]
ultimo = separa_nome[-1]
print("""Nome: {}
primeiro = {}
ultimo = {}""".format(nome, primeiro, ultimo))