import os
            

def cadastrar():
    if os.stat("nomes.txt").st_size == 0:
        nomes = open("nomes.txt", "w")
    else:
        nomes = open("nomes.txt", "a")
    print("-"*30)
    print("{:^30}".format("NOVO CADASTRO"))
    print("-"*30)
    nome = str(input("Nome: "))
    nomes.write(f"{nome}\n")
    while True:
        idade = input("Idade: ")
        if os.stat("idades.txt").st_size == 0:
            idades = open("idades.txt", "w")
        else:
            idades = open("idades.txt", "a")
        if idade.isnumeric():
            idades.write(f"{idade}\n")
            print(f"Novo registro de {nome} adicionado.")
            nomes.close()
            idades.close()
            break
        else:
            print("\033[0;31;40mERRO: por favor, digite um numero inteiro valido.\033[0;31;40m")

def listar():
    print("-"*40)
    print("{:^40}".format("PESSOAS CADASTRADAS"))
    print("-"*40)
    idades = open("idades.txt", "r")
    with open("nomes.txt") as nomes, open("idades.txt") as idades:
        for n, i in zip(nomes, idades):
            n = n.strip()
            i = i.strip()
            print("{:<19} {:>15} anos".format(n, i))


def menu():
    print("-"*30)
    print("{:^30}".format("MENU PRINCIPAL"))
    print("-"*30)
    print("\033[0;33;40m1 -\033[0;33;40m\033[0;36;40m Ver Pessoas Cadastradas\033[0;36;40m")
    print("\033[0;33;40m2 -\033[0;33;40m\033[0;36;40m Cadastrar Pessoas\033[0;36;40m")
    print("\033[0;33;40m3 -\033[0;33;40m\033[0;36;40m Sair do Sistema\033[0;36;40m")
    print("-"*30)
    opcao = 0
    while opcao != 3:
        opcao = int(input("\033[0;33;40mSua Opcao: \033[0;33;40m"))
        if opcao == 3:
            break
        if opcao > 3 or opcao < 1:
            print("\033[0;31;40mERRO! Digite uma opcao valida!\033[0;31;40m")
        elif opcao == 1:
            listar()
        elif opcao == 2:
            cadastrar()
        menu()