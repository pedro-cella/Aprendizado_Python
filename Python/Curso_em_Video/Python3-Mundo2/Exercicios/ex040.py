print("====== DESAFIO 40 ======")
print("""Sobre o programa: Crie um programa que leia duas notas de um aluno e calcule sua media,
mostrando uma mensagem no final, de acrodo com a media atingida:
- Media abaixo de 5.0: REPROVADO
- Media entre 5.0 e 6.9: RECUPERACAO
- Media 7.0 ou superior: APROVADO""")
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
media = (nota1 + nota2)/2
if media < 5.0:
    print("REPROVADO")
elif media >= 5.0 and media <= 6.9:
    print("RECUPERACAO")
else:
    print("APROVADO")