#Input: 
nums = [2,5,6,9,10]

#Output: 2



def findGCD(nums):

        a = max(nums)
        b = min(nums)
        
        # Algoritmo di Euclide
        while b > 0:
            resto = a % b
            a = b
            b = resto
            
        return a
    


p=findGCD(nums)
print(p)