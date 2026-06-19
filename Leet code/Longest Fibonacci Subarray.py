nums = [5,2,7,9,16]
#Output 5



def longestSubarray(nums):
    i=0
    x=0
    massimo=0
    while i<len(nums)-2:
        if nums[i]+nums[i+1]==nums[i+2]:
            i+=1
            x+=1

        else:
            if x>massimo:
                massimo=x
            x=0
            i+=1
    
    if x>massimo:
            massimo=x
            
    return  massimo+2

p=longestSubarray(nums)
print(p)

