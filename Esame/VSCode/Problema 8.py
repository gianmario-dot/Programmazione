# Problema 8

def disegna_triangolo(n, h, simb):

    if n%2==0:
        return 'Base deve essere dispari'
    

    spaz=h

   

    stringa1=spaz*' ' + simb

    print(stringa1)
    l=0
    for i in range(h-1):

        spaz_inter=i+1
      
        stringa2= (spaz-i-1)*' ' + simb + (spaz_inter+i)*' ' + simb
        print(stringa2)
        




    return 


n=int(input('Base='))
h=int(input('Altezza='))

simb=input('Simbolo cvhe si vuole usare=')

p=disegna_triangolo(n, h, simb)

