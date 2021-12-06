from random import randint
from time import sleep
print("====== DESAFIO 88 ======")
from random import randint
print("""Sobre o programa: Faca um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serao gerados e vai sortear 6 numeros entre 1 e 60
para cada jogo, cadastrando tudo em uma lista composta.""")
jogos = int(input("Quantos jogos voce quer que eu sorteie? "))
lista = list()
palpite = list()
total = 1
while total <= jogos:
  contador = 0
  while True:
      numero = randint(1, 60)
      if numero not in palpite:
          palpite.append(numero)
          contador += 1
      if contador >= 6:
          break
  palpite.sort()
  lista.append(palpite[:])
  palpite.clear()
  total += 1
print("-="*3, f"SORTEANDO {jogos} JOGOS", "-="*3)
for i, l in enumerate(lista):
    print(f"Jogos {i+1} - {l}")
    sleep(2)