def disegna_triangolo(n, h, simb):

    if n%2==0:
        return 'Base deve essere dispari'
    

    spaz=n//2

    stringa=''

    for i in range(h):
        

        stringa= (spaz-i)*' ' + simb*(i+1)
      


        print(stringa)
    
    



    return 


n=int(input('Base='))
h=int(input('Altezza='))

simb=input('Simbolo cvhe si vuole usare=')

p=disegna_triangolo(n, h, simb)
