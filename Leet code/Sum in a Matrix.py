#Input: 
nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]

#Output: 15



def matrixSum(nums):
    sum=0
    
    valori_i=[]
    for i in range(len(nums)):
        valori_i.append([])

    for i in range(len(nums)):
        nums[i].sort(reverse=True)

    for i in range(len(nums)):
        for j in range(len(nums[0])):
            valori_i[i].append(nums[i][j])

    for i in range(len(nums)):
        valori_i[i].sort(reverse=True)

    for i in range(len(nums)):
        sum+=valori_i[][i]
    

    return sum

p=matrixSum(nums)
print(p)