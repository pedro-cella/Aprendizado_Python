from random import randint
print("====== DESAFIO 100 ======")
print("""Sobre o programa: Faca um programa que tenha uma lista chamada numeros e duas funcoes chamadas sorteio()
e somaPar(). A primeira funcao vai sortear 5 numeros e vai coloca-los dentro da lista e a segunda funcao vai
mostrar a soma entre todos os valores PARES sorteados pela funcao anterior""")
lista = []
soma = 0
def sorteio():
    for i in range(0, 5):
        numero = randint(1, 100)
        lista.append(numero)


def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    return soma

sorteio()
print("Sorteando valores: ", end='')
for i in range(len(lista)):
    print(f"{lista[i]}", end=' ')
print("PRONTO!")
print(f"Somando os valores pares de {lista}, temos {somaPar(lista)}")