# Problema 7

import numpy as np

def ordinatore(l):

    n=len(l)

    for i in range(n):
        for j in range(n-1):
            if l[j]>l[j+1]:
                l[j], l[j+1]=l[j+1], l[j]


    return l


n=int(input('Lunghezza lista='))
lista=np.random.randint(0,100, size=n)


print(lista)

p=ordinatore(lista)
print(p)