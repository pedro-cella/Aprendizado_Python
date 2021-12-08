print("====== DESAFIO 99 ======")
print("""Sobre o programa: Faca um programa que tenha uma funcao chamada maior(), que recebe varios parametros
com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles e o maior.""")
def maior(* valores):
    print("-="*30)
    print("Analisando os valores passados...")
    if len(valores) == 0:
        print(f"Foram informados 0 valores ao todo.")
        print(f"O maior valor informado foi 0.")
    else:
        print(f"{valores} Foram informados {len(valores)} valores ao todo.")
        print(f"O maior valor informado foi {max(valores)}.")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()