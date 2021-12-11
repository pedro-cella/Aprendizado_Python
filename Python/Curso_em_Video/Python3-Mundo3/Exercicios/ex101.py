from datetime import date
print("====== DESAFIO 101 ======")
print("""Sobre o programa: Crie um programa que tenha uma funcao chamada voto() que vai receber como parametro o ano 
de nascimento de uma pessoa, retornando um valor literal indicando se a pessoa tem voto NEGADO,
OPICIONAL ou OBRIGATORIO nas eleicoes.""")
def voto(ano):
    idade = date.today().year - ano
    if idade < 18:
        return print(f"Com {idade} anos: NAO VOTA")
    elif idade >= 65:
        return print(f"Com {idade} anos: VOTO OPICIONAL")
    else:
        return print(f"Com {idade} anos: VOTO OBRIGATORIO")


print("-"*15)
ano_nascimento = int(input("Em que ano voce nasceu? "))
voto(ano_nascimento)