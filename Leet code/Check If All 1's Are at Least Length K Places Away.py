nums = [1,0,0,0,1,0,0,1]
#nums =[1,0,0,1,0,1]

k =2



def kLengthApart(nums, k):
    indici=[]
    valid=True 

    for j in range(len(nums)):
        if nums[j]==1:
            indici.append(j)

    for i in range(len(indici)-1):
        if indici[i+1]-indici[i]>=k+1:
            valid=True
        
        else: return False

    return valid



p=kLengthApart(nums, k)
print(p)
