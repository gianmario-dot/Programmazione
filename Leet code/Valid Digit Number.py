#Input: 
n = 232
x = 2

#Output: false

def validDigit(n, x):
        l=str(n)
        r=str(x)

        if l[0]==r:
            return False
        
        for i in l:
            if i==r:
                return True

        return False

            



  

p=validDigit(n, x)
print(p)