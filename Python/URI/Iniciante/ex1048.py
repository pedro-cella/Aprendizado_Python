valor = float(input())
conversor = "{:.2f}".format(valor)
salario = float(conversor)


if salario >= 0 and salario <= 400.00:
    reajuste = 15/100
elif salario >= 400.01 and salario <= 800.00:
    reajuste = 12/100
elif salario >= 800.01 and salario <= 1200.00:
    reajuste = 10/100
elif salario >= 1200.01 and salario <= 2000.00:
    reajuste = 7/100
else:
    reajuste = 4/100

novo_salario = salario + (salario*reajuste)
reajuste_ganho = salario*reajuste
percentual = reajuste*100


print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste gaho: {reajuste_ganho:.2f}")
print(f"Em percentual: {percentual:.0f} %")