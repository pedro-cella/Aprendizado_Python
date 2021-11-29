print("====== DESAFIO 22 ======")
print("""Sobre o projeto: Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiusculas;
- O nome com todas as letras minusculas;
- Quantas letras ao todo(sem considerar espacos;
- Quantas letras tem o primeiro nome;""")
nome = input("Insira o nome completo de uma pessoa: ")
nome_maisuculo = nome.upper()
nome_minusculo = nome.lower()
lista_nome = nome.split()
nome_sem_espaco = len(''.join(lista_nome))
primeiro_nome = len(lista_nome[0])

print("""Nome Completo: {}
Nome Completo com todas as letras maiusculas: {}
Nome Completo com todas as letras minusculas: {}
Total de letras no nome(sem espacos): {}
Total de Letras do primeiro nome: {}""".format(nome, nome_maisuculo, nome_minusculo, nome_sem_espaco, primeiro_nome))