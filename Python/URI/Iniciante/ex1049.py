primeira_palavra = input()
segunda_palavra = input()
terceira_palavra = input()

if primeira_palavra == 'vertebrado':
    if segunda_palavra == 'ave':
        if terceira_palavra == 'carnivoro':
            print("aguia")
        else: #onivoro
            print("pomba")
    else: # mamifero
        if terceira_palavra == 'onivoro':
            print("homem")
        else: #herbivoro
            print("vaca")
else: #invertebrado
    if segunda_palavra == 'inseto':
        if terceira_palavra == 'hematofago':
            print("pulga")
        else: #herbivoro
            print("lagarta")
    else: #anelideo
        if terceira_palavra == 'hematofago':
            print("sanguessuga")
        else: #onivoro
            print("minhoca")
    