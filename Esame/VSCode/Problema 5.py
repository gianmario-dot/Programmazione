# Problema 5

import numpy as np

def montecarlo(n , tentativi):
    
    n_max=n*6
    prob={}
  
        

    for i in range(tentativi):
        numero=np.random.randint(1, n_max)
        if numero in prob:
            prob[numero]+=1
        
        else:prob[numero]=0

    return prob


n=int(input('Numero di dadi'))

tentatvi=int(input('Numero di tentativi'))

p=montecarlo(n, tentatvi)
print(p)