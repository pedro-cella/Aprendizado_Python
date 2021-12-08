# def lin():
#     print("-" * 30)
# def titulo(txt):
#     print("-" * 30)
#     print(txt)
#     print("-" * 30)    


# Programa Principal
# titulo("    CURSO EM VIDEO    ")
# titulo("    APRENDA PYTHON    ")
# titulo("    GUSTAVO GUANABARA    ")
# def soma(a, b):
#     print(f"A = {a} e B = {b}")
#     s = a + b
#     print(f"A soma A + B = {s}")


# Programa Principal
# soma(b=4, a=5)
# soma(7, 2)
# soma(a=4, b=5)
# soma(8, 9)
# soma(2, 1)
# soma(4, 1)

# def contador(*num):
#     tam = len(num)
#     print(f"Recebi os valores {num} e sao ao todo {tam} numeros")

# contador(2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)

# def dobra(lst):
#     pos = 0
#     while pos < len(lst):
#         lst[pos] *= 2
#         pos += 1

# valores = [6, 3, 9, 1, 0, 2]
# dobra(valores)
# print(valores)

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f"Somando os valores {valores} temos {s}")

soma(5, 2)
soma(2, 9, 4)