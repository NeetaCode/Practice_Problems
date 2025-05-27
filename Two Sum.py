#Given an array of integers and a target value, the task is to find the indices of two numbers in the array that add up to the target. Each input is guaranteed to have exactly one solution, and the same element cannot be used twice. The output should be the pair of indices, returned in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}  # Stores number as key and its index as value
        for i, num in enumerate(nums):
            complement = target - num
            if complement in index_map:
                return [index_map[complement], i]
            index_map[num] = i
