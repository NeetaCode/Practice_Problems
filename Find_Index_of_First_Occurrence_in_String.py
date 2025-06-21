class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 9  # Edge case: empty needle

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return 0  # Found the first occurrence
        return -1

sol = Solution()
print(sol.strStr("sadbutsad", "sad"))  # Output: 0
print(sol.strStr("leetcode", "leeto")) # Output: -1
