#Input: 
nums = [2,1,1,1,1,2,2,3, 4, 4, 3, 3, 2, 1 ]

#Output: 2

def majorityElement(nums):
    apparizioni={}

    for i in nums:
        if i in apparizioni:
            apparizioni[i]+=1
        
        else: apparizioni[i]=1

    print(apparizioni)
    return max(apparizioni, key=apparizioni.get)


p=majorityElement(nums)
print(p)

                  