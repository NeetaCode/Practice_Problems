class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trn_str=strs[0]
        for i in range(1,len(strs)):
            j=0
            while j < len(trn_str) and j < len(strs[i]) and trn_str[j]==strs[i][j]:
                j += 1
                
            trn_str = trn_str[:j]

        print(trn_str)
        return trn_str
# Example tests:
sol = Solution()

print(sol.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(sol.longestCommonPrefix(["dog", "racecar", "car"]))     # Output: ""
