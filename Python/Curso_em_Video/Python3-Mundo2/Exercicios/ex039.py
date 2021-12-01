print("====== DESAFIO 39 ======")
print("""Sobre o programa: Faca um programa que leia o ano de nascimento de um jovem e informe, de
acordo com sua idade:
- Se ele ainda vai se alistar ao servico militar.
- Se e a hora de se alistar.
- Se ja passou do tempo do alistamento.
Seu programa tambem devera mostrar o tempo que faltou ou que passou do prazo.""")
ano_nascimento = int(input("Insira seu ano de nascimento: "))
idade = 2021 - ano_nascimento
if idade < 18:
    print("Voce ainda vai se alistar ao servico militar, faltam {} ano(s)".format(18-idade))
elif idade == 18:
    print("E hora de se alistar")
else:
    print("Voce ja passou do periodo para se alistar, ja se passaram {} ano(s)".format(idade - 18))