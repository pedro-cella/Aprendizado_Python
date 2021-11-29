print("====== DESAFIO 26 ======")
print("""Sobre o programa: Faca um programa que leia a frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A";
- Em que posicao ela aparece a primeira vez;
- Em que posicao ela aparece a penultima vez;""")
frase = input("Digite uma frase: ")
quantidade_a = frase.count("A")
primeiro_a = frase.find("A")
ultimo_a = frase.rfind("A")
print("""Quantidade de A: {}
Posicao que aparece a primeira vez: {}
Posicao que aparece a ultima vez: {}
""".format(quantidade_a, primeiro_a, ultimo_a))