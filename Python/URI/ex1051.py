valor = float(input())

if valor <= 2000.00:
    print("Isento")
elif valor >= 2000.01 and valor <= 3000.00:#8%
    valor -= 2000.00
    imposto = valor*(8/100)
    print("R$ {:.2f}".format(imposto))
elif valor >= 3000.01 and valor <= 4500.00:#18%
    valor -= 2000.00
    resto = valor-1000.00
    valor = 1000.00
    imposto = valor*(8/100)
    imposto += resto*(18/100)
    print("R$ {:.2f}".format(imposto))
elif valor > 4500.00:#28%
    valor -= 2000.00
    valor -= 1000.00
    imposto = 1000*(8/100)
    valor -= 1500.00
    imposto += 1500*(18/100)
    imposto += valor*(28/100)
    print("R$ {:.2f}".format(imposto))

# 4520
# 2000 = Isento -> 2520
# 1000 = 8% -> 1520
# 1500 = 18% -> 20
# 20 - 28%
# Soma = (1000*8%) + (1500 * 18%) + (20*28%)

# 3002.00
# 2000.00 = Isento -> 1002.00
# 1000.00 = 8% -> 80
# 2.00 = 18% -> 0.36

# Outra forma

# r = float(input())

# if r <= 2000.00:
#     i = 0
#     print('Isento')
    
# if 2000.00 < r <= 3000.00:
#     r8 = r - 2000.00
#     i = r8 * (8 / 100)
    
# if 3000.00 < r <= 4500.00:
#     i8 = (8 / 100) * (1000.00)
#     r18 = r - 3000.00
#     i = r18 * (18 / 100) + i8
    
# if r > 4500.00:
#     i8 = (8 / 100) * (1000.00)
#     i18 = (18 / 100) * (1500.00)
#     r28 = r - 4500.00
#     i = i18 + i8 + r28 * (28 / 100)

# if r > 2000.00:
#     i = float(i)
#     print('R$ {:.2f}'.format(i))