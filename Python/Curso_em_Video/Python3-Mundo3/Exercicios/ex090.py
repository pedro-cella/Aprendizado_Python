print("====== DESAFIO 90 ======")
print("""Sobre o programa: Faca um programa que leia nome e media de um aluno, guardando tambem a situacao
em um dicionario. No final, mostre o conteudo da estrutura na tela.""")
situacao = dict()
nome = input("Nome: ")
media = float(input(f"Media de {nome}: "))
situacao = {'aprovado': 'Aprovado', 'reprovado': 'Reprovado'}
print(f"Nome e igual a {nome}")
print(f"Media e igual a {media}")
if media >= 5:
    print(f"Situacao e igual a {situacao['aprovado']}")
else:
    print(f"Situacao e igual a {situacao['reprovado']}")