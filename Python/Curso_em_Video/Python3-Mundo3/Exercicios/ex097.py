print("====== DESAFIO 97 ======")
print("""Sobre o programa: Faca um programa que tenha uma funcao chamada escreva(), que recebe um texto
qualquer como parametro e mostre uma mensagem com tamanho adaptavel.""")
def escreva(texto):
    print("~"*(7+len(texto)))
    print(f"   {texto}   ")
    print("~"*(7+len(texto)))


escreva("Gustavo Guanabara")
escreva("Curso de Python no YouTube")
escreva("CeV")