# Problema 9

def distanza_massima_carattere(s, car):

    dist=0
    index=[]
    if car not in s:
        return 'Carattere non presente'
    
    for i in range(len(s)):
        if s[i]==car:
               index.append(i)
    
    dist=index[-1]-index[0]

    return dist

car=input('carattere cercato=')

s='ciaooaic'


p=distanza_massima_carattere(s, car)
print(p)