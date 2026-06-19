# Problema 10



def n_raggi_laser(bank):
    n_punt=[]
    collegamenti=0

    for i in range(len(bank)):
        n_punt.append(0)

        for j in range(len(bank[0])):
            if bank[i][j]==1:
               n_punt[i]+=1

    for x in range(len(n_punt)-1):
        if n_punt[x]==0:
            n_punt.pop(x)

    for i in range(len(n_punt)-1):
        collegamenti+=n_punt[i]*n_punt[i+1]



    return collegamenti, n_punt



bank=[[0,1,1,0,0,1], [0,0,0,0,0,0], [0,1,0,1,0,0], [0,0,1,0,0,0]]

bank=[[0,0,0], [1,1,1], [0,0,0]]


p, n=n_raggi_laser(bank)
print(p)
print(n)