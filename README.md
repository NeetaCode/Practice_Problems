___________________________________________________________________________________________________________________________________________________________________
# DSA_Roadmap
___________________________________________________________________________________________________________________________________________________________________

# Week 1: Arrays, Hash Maps & Patterns
# Goal: Build strong foundation

**Arrays & Hash Maps**
- Two Sum (LC#1) → Done
- Contains Duplicate (LC#217) → Done
- Valid Anagram (LC#242) --> Done
- Product of Array Except Self (LC#238)
- Top K Frequent Elements (LC#347)
- Group Anagrams (LC#49)
- Longest Consecutive Sequence (LC#128)
- Encode and Decode Strings (LC#659)
- Maximum Number of Ways to Partition an Array
- Number of Subarrays That Match a Pattern II

**Other Array/String Problems**
- Palindrome Number → Done
- Search Insert Position → Done
- Roman to Integer → Done
- Remove Element → Done
- Remove Duplicates from Sorted Array → Done
- Longest Common Prefix → Done
- Length of Last Word → Done
- Find Index of First Occurrence in String → Done
___________________________________________________________________________________________________________________________________________________________________

# Week 2: Recursion + Trees + Sliding Window
# Goal: Strengthen mid-level concepts

**Recursion**
- Climbing Stairs (LC#70) → Done
- Generate Parentheses (LC#22) → Done
- Permutations (LC#46)
- Letter Combinations of a Phone Number (LC#17)
- Combination Sum (LC#39)

**Trees**
- Maximum Depth of Binary Tree (LC#104) → Done
- Invert Binary Tree (LC#226)
- Validate Binary Search Tree (LC#98)
- Lowest Common Ancestor of a Binary Tree (LC#236)
- Binary Tree Paths (LC#257)

**Sliding Window**
- Minimum Size Subarray Sum (LC#209) → Done
- Longest Substring Without Repeating Characters (LC#3)
- Permutation in String (LC#567)
- Longest Repeating Character Replacement (LC#424)
- Find All Anagrams in a String (LC#438)
___________________________________________________________________________________________________________________________________________________________________

# Week 3: Dynamic Programming (DP)
# Goal: Learn common problem-solving patterns

**Top 8 DP Problems**
- Climbing Stairs (LC#70) → Done
- House Robber (LC#198)
- Longest Common Subsequence (LC#1143)
- Partition Equal Subset Sum (LC#416)
- Target Sum (LC#494)
- House Robber II (LC#213)
- Edit Distance (LC#72)
- Longest Increasing Subsequence (LC#300)
___________________________________________________________________________________________________________________________________________________________________


# Week 4: Mock Interviews + Pattern Review  
# Goal: Simulate interview settings & reinforce patterns
- Mix of problems from Weeks 1–3 under time pressure.
- Focus on review, speed, and accuracy.
___________________________________________________________________________________________________________________________________________________________________
# Miscellaneous
# Simpler Codefor Two Sum.py:

Simpler Code:
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    sum = nums[i] + nums[j]
                    if sum == target:
                        return [i, j]


```
_____________________________________________________________________________________________________________________________________  
LeetCode Prep  
_____________________________________________________________________________________________________________________________________  
Organized by topic and difficulty. Focused on questions frequently asked in interviews for SWE roles.  


🌳 Graph / Trees  
Easy  
[94] Binary Tree Inorder Traversal--> Done  
[144] Binary Tree Preorder Traversal--> Done  
[145] Binary Tree Postorder Traversal--> Done  
[261] Graph Valid Tree (medium to easy)--> Done  

Medium  
[127] Word Ladder  
[236] Lowest Common Ancestor of Binary Tree  
[323] Number of Connected Components in Graph  
[1650 / 1696] Cycle Detection / Advanced LCA Variants  


📊 Dynamic Programming  
Easy  
[70] Climbing Stairs (also under recursion)  --> Done  
[338] Counting Bits  --> Done  
[121] Best Time to Buy and Sell Stock I  

Medium  
[139] Word Break  
[309] Best Time to Buy and Sell Stock with Cooldown  
[329] Longest Increasing Path in a Matrix  
[63] Unique Paths II  


🔤 Arrays & String Processing  
Easy  
[1] Two Sum  --> Done  
[53] Maximum Subarray  --> Done  
[49] Group Anagrams  

Medium  
[3] Longest Substring Without Repeating Characters  
[15] 3Sum  
[1408] String Matching in an Array  


🔁 Recursion / Backtracking  
Easy  
[70] Climbing Stairs  
[206] Reverse Linked List (via recursion)  

Medium  
[22] Generate Parentheses  
[46] Permutations  
[78] Subsets  


🛠️ System Design (LeetCode-Style)   
These aren’t classic DSA problems but involve modeling and system architecture thinking.  
[535] Encode and Decode TinyURL  
[1396] Design Underground System  


📐 Geometry / Math  
Easy  
[9] Palindrome Number  
[12] Integer to Roman  
[13] Roman to Integer  

Medium  
[241] Different Ways to Add Parentheses (math + recursion + DP)  
[~1232] Circle Overlap / Max Area Triangle (search by tags)  


Example Repos: https://github.com/xizhang20181005/Leetcode_company_frequency

