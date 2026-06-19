#Input: 
num1 = "1-1i"
num2 = "1+1i"

#Output: "0-2i"


def complexNumberMultiply(num1, num2):
    n1=[]
    n2=[]
    n3=[]
    mult=''
    i=0
    j=0

    while i<len(num1):
        try:
            x=int(num1[i])
            n1.append(x)
            i+=1
    
        except:
            if num1[i]=='-':
                n1.append(int(num1[i]+num1[i+1]))
                i+=2
            else: i+=1
    
    while j<len(num1):
        try:
            x=int(num2[j])
            n2.append(x)
            j+=1
    
        except:
            if num2[j]=='-':
                n2.append(int(num2[j]+num2[j+1]))
                j+=2
            else: i+=1

    n3.append(n1[0]*n2[0])
    n3.append(n1[0]*n2[1])
    n3.append(n1[1]*n2[0])
    n3.append(n1[1]*n2[1])

    reale=n3[0]-n3[3]
    imm=n3[1]+n3[2]

    mult=str(reale)+'+'+str(imm)+'i'

    return mult


p=complexNumberMultiply(num1, num2)
print(p)