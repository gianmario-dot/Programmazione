#Input: 
n = 1234567
#n=987

#Output: "1.234"


def thousandSeparator(n):

    stringa=str(n)
    lun=len(stringa)
    commas=[]
    j=3
    coso=lun
    while j<lun:
        if lun-j>0:
            coso=lun-j
            commas.append(coso)
            j+=3
        else: break

    output=''
    i=0
    if lun>3:
        while i<lun:
            if i not in commas:
                output+=stringa[i]
                i+=1
            else: 
                output+='.'
                output+=stringa[i]
                i+=1
    
    else:   
            while i<lun:

                    output+=stringa[i]
                    i+=1

    return output



p=thousandSeparator(n)
print(p)