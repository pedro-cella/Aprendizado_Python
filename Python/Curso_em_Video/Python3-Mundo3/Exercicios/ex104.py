print("====== DESAFIO 104 ======")
print("""Sobre o programa: Crie um programa que tenha a funcao leiaInt(), que vai funcionar de forma
semelhante a funcao input() do Python, so que fazendo a validacao para aceitar apenas um valor numerico.
Ex: n = leiaInt('Digite um n')""")
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[0;31mERROR! Digite um numero inteiro valido.\033[m")
        if ok:
            break
    return valor
        


n = leiaInt('Digite um numero: ')
print(f"Voce acabou de digitar o numero {n}")