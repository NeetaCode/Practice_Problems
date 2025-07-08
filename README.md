____________________________________________________________________________________________________________________________________________________________________________________________________________________
**DSA_Roadmap**
____________________________________________________________________________________________________________________________________________________________________________________________________________________

**Week 1: Arrays, Hash Maps & Patterns
Goal: Build strong foundation**

**Arrays & Hash Maps**
Two Sum (LC#1) → Done
Contains Duplicate (LC#217) → Done
Valid Anagram (LC#242)
Product of Array Except Self (LC#238)
Top K Frequent Elements (LC#347)
Group Anagrams (LC#49)
Longest Consecutive Sequence (LC#128)
Encode and Decode Strings (LC#659)
Maximum Number of Ways to Partition an Array
Number of Subarrays That Match a Pattern II

**Other Array/String Problems**
Palindrome Number → Done
Search Insert Position → Done
Roman to Integer → Done
Remove Element → Done
Remove Duplicates from Sorted Array → Done
Longest Common Prefix → Done
Length of Last Word → Done
Find Index of First Occurrence in String → Done
____________________________________________________________________________________________________________________________________________________________________________________________________________________

**Week 2: Recursion + Trees + Sliding Window
Goal: Strengthen mid-level concepts**

**Recursion**
Climbing Stairs (LC#70) → Done
Generate Parentheses (LC#22) → Done
Permutations (LC#46)
Letter Combinations of a Phone Number (LC#17)
Combination Sum (LC#39)

**Trees**
Maximum Depth of Binary Tree (LC#104) → Done
Invert Binary Tree (LC#226)
Validate Binary Search Tree (LC#98)
Lowest Common Ancestor of a Binary Tree (LC#236)
Binary Tree Paths (LC#257)

**Sliding Window**
Minimum Size Subarray Sum (LC#209) → Done
Longest Substring Without Repeating Characters (LC#3)
Permutation in String (LC#567)
Longest Repeating Character Replacement (LC#424)
Find All Anagrams in a String (LC#438)
____________________________________________________________________________________________________________________________________________________________________________________________________________________

**Week 3: Dynamic Programming (DP)
Goal: Learn common problem-solving patterns**

**Top 8 DP Problems**
Climbing Stairs (LC#70) → Done
House Robber (LC#198)
Longest Common Subsequence (LC#1143)
Partition Equal Subset Sum (LC#416)
Target Sum (LC#494)
House Robber II (LC#213)
Edit Distance (LC#72)
Longest Increasing Subsequence (LC#300)
____________________________________________________________________________________________________________________________________________________________________________________________________________________


**Week 4: Mock Interviews + Pattern Review**
Goal: Simulate interview settings & reinforce patterns**
Mix of problems from Weeks 1–3 under time pressure
Focus on review, speed, and accuracy
____________________________________________________________________________________________________________________________________________________________________________________________________________________

**Miscellaneous**
# Simpler Codefor Two Sum.py:

Simpler Code:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    sum = nums[i] + nums[j]
                    if sum == target:
                        return [i, j]
