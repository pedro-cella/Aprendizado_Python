import requests
print("====== DESAFIO 114 ======")
print("""Sobre o programa: Crie um codigo em Python que teste se o site Pudim esta acessivel pelo computador usado.""")
try:
    r = requests.get('http://pudim.com.br/')
except:
    print("\033[0;31;40mO site Pudim nao esta acessivel no momento\033[0;31;40m")
else:
    print("\033[0;32;40mConsegui acessar o site Pudim com sucesso\033[0;32;40m")