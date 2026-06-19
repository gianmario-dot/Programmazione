# Problema 4

import numpy as np


def calcola_antidiagonale(x):

    AntiDiag=0

    for i in range(n):
        AntiDiag+=x[i, n-i-1]




    return AntiDiag    



n=int(input('Dimensione matrice='))

x=np.random.randint(0,100, size=(n,n))


p=calcola_antidiagonale(x)
print(x)
print(p)


