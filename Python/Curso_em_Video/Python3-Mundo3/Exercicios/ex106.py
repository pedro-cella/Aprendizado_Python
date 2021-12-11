from time import sleep
print("====== DESAFIO 106 ======")
print("""Sobre o programa: Faca um mini-sistema que utilize o Interactive Help do Python.
O usuario vai digitar o comando e o manual vai aparecer.
Quando o usuario digitar 'FIM', o programa se encerrara.
OBS: Use cores.""")
def ajuda(com):
    print("~"*20)
    print(f"Acessando o manual do comando '{com}'")
    print("~"*20)
    sleep(2)
    help(com)

def titulo():
    print("~"*20)
    print("SISTEMA DE AJUDA PyHELP")
    print("~"*20)

while True:
    titulo()
    comando = input("Funcao ou Biblioteca > ")
    if comando.upper() == 'FIM':
        break
    ajuda(comando)
print("~"*10)
print("ATE LOGO")
print("~"*10)