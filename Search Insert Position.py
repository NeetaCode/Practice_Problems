class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        result = 0  # will hold the final index

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                return result
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        result = left  # insertion point
        return result      
