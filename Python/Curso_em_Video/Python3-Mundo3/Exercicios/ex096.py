print("====== DESAFIO 96 ======")
print("""Sobre o programa: Faca um programa que tenha uma funcao chamada area(), que recebe as
dimensoes de um terreno retangular (largura e comprimento) e mostre a area do terreno.""")
def area(largura, comprimento):
    print(f"A area de um terreno {largura}x{comprimento} e de {largura*comprimento}m^2.")


print("  Controle de Terrenos")
print("-"*23)
largura = float(input("LARGURA (m): "))
comprimento = float(input("COMPRIMENTO (m): "))
area(largura, comprimento)
