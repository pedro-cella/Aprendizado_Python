print("====== DESAFIO 36 ======")
print("""Sobre o programa: Escreva um programa para aprovar o emprestimo
bancario para a compra de uma casa. O programa vai perguntar o valor da casa, o salario do comprador
e em quantos anos ele vai pagar.
Calcule o valor da prestacao mensal, sabendo que ela nao pode exceder 30% do salario
ou entao o emprestimo sera negado.""")
valor_casa = float(input("Qual o valor da casa? "))
salario = float(input("Quanto e o valor do seu salario?  R$"))
anos = int(input("Em quantos anos voce deseja pagar a casa? "))
meses = anos*12
parcela_mensal = valor_casa/meses
if parcela_mensal > (salario*(30/100)):
    print("Seu emprestimo foi negado!")
else:
    print("Parabens! Seu emprestimo foi aceito")