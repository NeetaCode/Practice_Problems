#Given an array of integers and a target value, the task is to find the indices of two numbers in the array that add up to the target. Each input is guaranteed to have exactly one solution, and the same element cannot be used twice. The output should be the pair of indices, returned in any order.

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        
        for i in range(len(nums)):
            res[nums[i]] = i
        
        #print(res)
        
        for i in range(len(nums)):
            y = target - nums[i]
            # print("y",y)
            #9-2=7--> TC 1, when i=0
            # TC 2, when i=0, y=6-3=3, y=3
            if y in res and res[y] != i:
                print([i, res[y]])
                #7 in {2: 0, 7: 1, 11: 2, 15: 3} and res[7]!=0--> TC 1, when i=0
                # TC 2, when i=0, 3 in {3: 0, 2: 1, 4: 2} and res[3] != 0, but here 0 = 0
                return [i, res[y]]
    
s = Solution()    
s.twoSum([2,7,11,15],9)
s.twoSum([3,2,4],6)
s.twoSum([3,3],6)
