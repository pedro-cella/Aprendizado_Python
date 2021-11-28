from random import shuffle
print("====== DESAFIO 20 ======")
print("Sobre o programa: O mesmo professor do desafio anterior quer sortear a ordem", end='')
print(" de apresentacao dos trabalhos dos alunos. Faca um programa que leia o nome dos quatro alunos", end='')
print(" e mostra a ordem sorteada")
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print("A ordem de apresentacoes e: \n", end='')
print("1- {}\n2- {}\n3- {}\n4- {}".format(lista[0], lista[1], lista[2], lista[3]))