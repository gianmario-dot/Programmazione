# Problema 3

def masismo_minimo_media(l):
    n=len(l)
    somma=0

    for i in range(n):
        for j in range(n-1):
            if l[j]>l[j+1]:
                l[j], l[j+1]=l[j+1], l[j]

    Max=l[-1]
    Min=l[0]

    for i in l:
        somma+=i

    Med=somma/n


    return Max, Min, Med

lista=[1,2,3,4,5,6, 56, 33, 56, 78, 55, 79, 34, 89, 99]
M,m, med=masismo_minimo_media(lista)
print('massimo=',M, 'minimo=',m , 'media=',med)

l=masismo_minimo_media(lista)
print(l)