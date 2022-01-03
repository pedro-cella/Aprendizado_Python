dia_inicial = int(input().split()[1])

hora_i = input().split(":")
hora_inicial = int(hora_i[0])
minuto_inicial = int(hora_i[1])
segundo_inicial = int(hora_i[2])

dia_final = int(input().split()[1])

hora_f = input().split(":")
hora_final = int(hora_f[0])
minuto_final = int(hora_f[1])
segundo_final = int(hora_f[2])

inicio = segundo_inicial + minuto_inicial*60 + hora_inicial*(60*60) + dia_inicial*(60*60*24)
fim = segundo_final + minuto_final*60 + hora_final*(60*60) + dia_final*(60*60*24)
if inicio < fim:
    tempo = fim - inicio
    dia_total = int(tempo/(60*60*24))
    tempo = tempo%(60*60*24)
    hora_total = int(tempo/(60*60))
    tempo = tempo%(60*60)
    minuto_total = int(tempo/60)
    tempo = tempo%60
    segundo_total = tempo

print(f"{dia_total} dia(s)")
print(f"{hora_total} hora(s)")
print(f"{minuto_total} minuto(s)")
print(f"{segundo_total} segundo(s)")