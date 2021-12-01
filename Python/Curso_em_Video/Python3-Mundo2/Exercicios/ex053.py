print("====== DESAFIO 53 ======")
print("""Sobre o programa: Crie um programa que leia uma frase qualquer e diga se ela e um palindromo
desconsiderando os espacos""")
# Minha Solucao
# frase = input("Insira uma frase: ")
# lista = frase.split()
# frase_sem_espaco = ''.join(lista).upper()
# frase_ao_contrario = frase_sem_espaco[::-1]
# if frase_sem_espaco == frase_ao_contrario:
#     print("A frase {} e um palindromo".format(frase))
# else:
#     print("A frase {} nao e um palindromo".format(frase))

# Outra solucao
frase = input("Insira uma frase: ")
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print("Temos um palindromo")
else:
    print("A frase digitada nao e um palindromo")