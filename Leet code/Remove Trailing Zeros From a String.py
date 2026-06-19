num ="51230100"


def removeTrailingZeros(num):
    i=0
    n=len(num)
    output=''
    while True:
        if num[n-i-1]=='0':
            i+=1
        else:
            for j in range(n-i):
                output+=num[j]
            
            return output


p=removeTrailingZeros(num)
print(p)