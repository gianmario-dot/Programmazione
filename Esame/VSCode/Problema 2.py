# Problema 2

def contavocali(s, diz):


    for i in s:
        if i in diz:
            diz[i]+=1

   

    return diz


s='scrivere funzione che conta quante volte ciascuna vocale'

diz={'a':0,'e':0,'i':0,'o':0,'u':0}

contavocali(s, diz)

print(diz)