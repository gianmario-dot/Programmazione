# Problema 1

def primiventimultipli(n, m, ):

    multipli=[]
    i=0

    while True:
        if len(multipli)==20:
            return multipli
        
        else: 
            if (n*i)%m!=0:
                multipli.append(n*i)
                i+=1

            else: i+=1
    


    return   multipli



n=int(input('Valore di n='))
m=int(input('Valore di m='))

if m<n:
    print('n deve essere minore di m')


p=primiventimultipli(n,m)
print(p)