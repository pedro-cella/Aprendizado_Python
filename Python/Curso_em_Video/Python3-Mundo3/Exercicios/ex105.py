print("====== DESAFIO 105 ======")
print("""Sobre o programa: Faca um programa que tenha uma funcao notas() que pode receber varias notas
de alunos e vai retornar um dicionario com as seguintes informacoes:
- Quantidade de notas
- A maior nota
- A menor nota
- A media da turma
- A situacao(opicional)
Adicione tambem as docstrings das funcoes""")
resultado = {}
media = 0
soma = 0
def notas(*notas, sit=False):
    """
    -> Funcao para analisar notas e situacoes de varios alunos.
    :param notas: uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opicional, indicando se deve ou nao adicionar a situacao
    :return: dicionario com varias informacoes sobre a situacao da turma.
    """
    global soma
    total = len(notas)
    resultado['total'] = total
    maior = max(notas)
    resultado['maior'] = maior
    menor = min(notas)
    resultado['menor'] = menor
    for i in notas:
        soma += i
    media = soma/total
    resultado['media'] = media
    if sit == True:
        if media >= 7:
            resultado['situacao'] = 'BOA'
        elif media >= 5 and media < 7:
            resultado['situacao'] = 'RAZOAVEL'
        else:
            resultado['situacao'] = 'RUIM'
    return resultado

resp = notas(3.5, 2, 6.5, sit=True)
print(resp)
help(notas)