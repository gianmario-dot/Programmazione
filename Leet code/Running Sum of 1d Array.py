def somma_ricorsiva(lista):
    # Caso base: se la lista è vuota, la somma è 0
    if not lista:
        return 0
    
    # Passo ricorsivo: somma il primo elemento con la somma del resto della lista
    return lista[0] + somma_ricorsiva(lista[1:])

# Esempio di utilizzo
numeri = [1, 2, 3, 4, 5]
totale = somma_ricorsiva(numeri)

print(f"La somma della lista {numeri} è: {totale}")
