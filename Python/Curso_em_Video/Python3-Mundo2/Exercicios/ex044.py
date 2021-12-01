print("====== DESAFIO 44 ======")
print("""Sobre o programa: Elabore um programa que calcule o valor a ser pago por um produto
, considerando o seu preco normal e condicao de pagamento:
- a vista dinheiro/cheque: 10% de desconto
- a vista no cartao: 5% de desconto
- em ate 2x no cartao: preco normal
- 3x ou mais no cartao: 20% de juros""")
preco = float(input("Insira o preco do produto: "))
print("""Escolha a forma de pagamento: 
1- A vista dinheiro/cheque
2- A vista no cartao
3- Ate 2x no cartao
4- Ate 3x ou mais no cartao""")
escolha = int(input("Escolha: "))
if escolha == 1:
    print("Voce escolheu pagar a vista dinheiro/cheque")
    desconto = preco*(10/100)
    preco_com_desconto = preco - desconto
    print("Com um desconto de 10% voce pagara {}".format(preco_com_desconto))
elif escolha == 2:
    print("Voce escolheu pagar a vista no cartao")
    desconto = preco*(5/100)
    preco_com_desconto = preco - desconto
    print("Com um desconto de 10% voce pagara {}".format(preco_com_desconto))
elif escolha == 3:
    print("Voce escolheu pagar ate 2x no cartao")
    print("Sem desconto, voce pagara {}".format(preco))
else:
    print("Voce escolheu pagar 3x ou mais no cartao")
    juros = preco*(20/100)
    preco_com_juros = preco + juros
    print("Com juros de 20% voce pagara {}".format(preco_com_juros))