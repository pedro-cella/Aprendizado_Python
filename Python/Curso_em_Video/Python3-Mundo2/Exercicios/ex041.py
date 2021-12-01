import datetime
print("====== DESAFIO 41 ======")
print("""Sobre o programa:  A Condeferacao NAcional de Natacao precisa de um programa que leia 
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Ate 9 anos: MIRIM;
- Ate 14 anos: INFANTIL;
- Ate 19 anos: JUNIOR;
- Ate 20 anos: SENIOR;
- Acima: MASTER""")
ano_nascimento = int(input("Insira o ano de nascimento: "))
ano_atual = datetime.datetime.now()
idade = ano_atual.year - ano_nascimento
if idade <= 9:
    print("MIRIM")
elif idade <= 14:
    print("INFANTIL")
elif idade <= 19:
    print("JUNIOR")
elif idade <= 20:
    print("SENIOR")
else:
    print("MASTER")