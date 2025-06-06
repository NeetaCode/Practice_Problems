from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        unique_pops = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[unique_pops] = nums[i]
                unique_pops += 1

        return unique_pops
