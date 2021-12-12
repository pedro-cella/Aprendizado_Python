def leiaDinheiro(valor):
    ok = False
    valor = 0
    while True:
        n = str(input("Digite o preco: R$"))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[0;31mERROR! {} e um preco invalido!\033[m".format(n))
        if ok:
            break
    return valor