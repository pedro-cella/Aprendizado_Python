print("====== DESAFIO 23 ======")
print("""Faca um programa que leia um numero de 0 a 9999 e mostre
na tela cada um dos digitos separados.
Ex: Digite um numero: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1""")
numero = int(input("Digite um numero entre 0 e 9999: "))
string = str(numero)

print("\nSolucao matematica")
numero_unidade = numero%10
numero = numero//10
numero_dezena = numero%10
numero = numero//10
numero_centena = numero%10
numero = numero//10
numero_milhar = numero%10
numero = numero//10
print("""unidade: {}
dezena: {}
centena: {}
milhar: {}\n""".format(numero_unidade, numero_dezena, numero_centena, numero_milhar))

print("Solucao String")
print("""unidade: {}
dezena: {}
centena: {}
milhar: {}""".format(string[3], string[2], string[1], string[0]))
