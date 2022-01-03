hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

total_hora = hora_final - hora_inicial
total_minutos = minuto_final - minuto_inicial

if total_minutos < 0:
    total_minutos += 60
    total_hora -= 1

if total_hora < 0:
    total_hora += 24

if total_hora == 0 and total_minutos == 0:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print(f"O JOGO DUROU {total_hora} HORA(S) E {total_minutos} MINUTO(S)")