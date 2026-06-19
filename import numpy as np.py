import numpy as np

nums = [10, 20, 30, 40, 50]
ris=0
for i in range(len(nums)):
    if i%2==0:
        ris+=nums[i]

    else: ris-=nums[i]

print(ris)