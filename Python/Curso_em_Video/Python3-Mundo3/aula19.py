# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# del pessoas['sexo']
# pessoas['nome'] = 'Leandro'
# pessoas['peso'] = 98.5
# print(pessoas['idade'])
# print(f"{pessoas['nome']} tem {pessoas['idade']}")
# print(pessoas.values())
# for k in pessoas.keys():
#     print(k)
# for v in pessoas.values():
#     print(v)
# for k, v in pessoas.items():
#     print(f"{k} = {v}")
# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'Sao Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil[0])
# print(brasil[0]['uf'])
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado['sigla'] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())
print(brasil)
# for e in brasil:
#     # print(e)
#     for k, v in e.items():
#         print(f"O campo {k} tem valor {v}.")

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()