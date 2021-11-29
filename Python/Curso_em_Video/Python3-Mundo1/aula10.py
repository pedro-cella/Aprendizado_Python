# nome = str(input("Qual e seu nome? "))
# if nome == 'Gustavo':
#     print("Que nome lindo voce tem!")
# else:
#     print("Seu nome e tao normal!")
# print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua media foi {:.1f}'.format(m))
print('PARABENS' if m >= 6 else 'ESTUDA MAIS!')