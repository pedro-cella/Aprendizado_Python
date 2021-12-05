print("====== DESAFIO 77 ======")
print("""Sobre o programa: Crie um programa que tenha uma tupla com varias palavras(nao use acentos).
Depois disso, voce deve mostrar, para cada palavra, quais sao as suas vogais""")
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
vogais = ('a', 'e', 'i', 'o', 'u')
# for contador, palavra in enumerate(palavras):
#     print(f"Na palavra {palavra.upper()} temos {[each for each in palavra if each in vogais]}")
for p in palavras:
    print(f"\nNa palavra {p.upper()} temos ", end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
print("\n")