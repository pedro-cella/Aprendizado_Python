print("====== DESAFIO 113 ======")
print("""Sobre o programa: Reescreva a funcao leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade
da digitacao de um numero de tipo invalido. Aproveite e crie tambem uma funcao leiaFloat() com a mesma funcionalidade.""")
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um numero inteiro valido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[31mUsuario preferiu nao digitar esse numero.\033[m")
            return 0
        else:
            return n
            
        
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um numero inteiro valido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[31mUsuario preferiu nao digitar esse numero.\033[m")
            return 0
        else:
            return n

n1 = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat("Digite um Real: ")
print(f"O valor inteiro digitado foi {n1} e o real foi {n2}")