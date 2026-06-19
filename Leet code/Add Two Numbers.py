#Input: 
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

#Output: [8,9,9,9,0,0,0,1]




def addTwoNumbers(l1, l2):
    if len(l1)>len(l2):
        corta=l2
        lunga=l1
    
    else:
        corta=l1
        lunga=l2

    n_c=len(corta)-1
    n_l=len(lunga)-1

    for i in range(n_c):
        lunga[n_l-i]+=corta[n_c-i]
        try:
            if lunga[n_l-i]==10:
                lunga[n_l-i]=0
                lunga[n_l-i-1]+=1
        
        except:
            if lunga[n_l-i]==10:
                lunga[n_l-i]=0
                lunga.append(1, 0)
    
    return lunga





p=addTwoNumbers(l1, l2)
print(p)