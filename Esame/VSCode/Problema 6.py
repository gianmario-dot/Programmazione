# Problema 6

def somma_ricorsiva(lista):

    if not lista:
        return 0
    
    return lista[0] + somma_ricorsiva(lista[1:])



lista = [1, 2, 3, 4, 5]

print(somma_ricorsiva(lista))


