“Arrays & Hash Maps” pattern problems

__________________________________________________________________________________
# Two Sum.py:
#Given an array of integers and a target value, the task is to find the indices of two numbers in the array that add up to the target. Each input is guaranteed to have exactly one solution, and the same element cannot be used twice. The output should be the pair of indices, returned in any order.

Simpler Code:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    sum = nums[i] + nums[j]
                    if sum == target:
                        return [i, j]
# Contains Duplicate.py
#This code checks if a list contains any duplicate values. It uses a set to track seen numbers and returns True if a duplicate is found; otherwise, it returns False.

# Two Sum (LC#1)--> Done
Find indices of two numbers that add up to a target using a single-pass hash map in O(n) time

# Contains Duplicate (LC#217)--> Done
Detect whether any value appears twice by storing seen elements in a hash set

# Valid Anagram (LC#242)--> Done
Check if two strings are anagrams by comparing hash maps or character counts 

# Product of Array Except Self (LC#238)
Compute products excluding each index without using division (prefix/product patterns) 

# Top K Frequent Elements (LC#347)
Use a hash map to count frequencies, then extract the top‑k elements efficiently 

# Group Anagrams (LC#49)
Group strings by sorted key or character-count key using a hash map

# Longest Consecutive Sequence (LC#128) – Find max consecutive run using a hash set 

# Encode and Decode Strings (LC#659) – Apply hashing strategies to support serialization 

# Maximum Number of Ways to Partition an Array – Uses prefix sums with hash maps 

# Number of Subarrays That Match a Pattern II – Analyze subarrays for specific increase/decrease patterns; mixes arrays and pattern detection 

__________________________________________________________________________________


# Recursion:
# Climbing Stairs (Easy) - #70 --> Done
# Generate Parentheses (Medium) - #22 --> Done
# Permutations (Medium) - #46
# Letter Combinations of a Phone Number (Medium) - #17
# Combination Sum (Medium) - #39

# Trees:
# Maximum Depth of Binary Tree (Easy) - #104 --> Done
# Invert Binary Tree (Easy) - #226
# Validate Binary Search Tree (Medium) - #98
# Lowest Common Ancestor of a Binary Tree (Medium) - #236
# Binary Tree Paths (Easy) - #257

# Sliding Window:
# Minimum Size Subarray Sum (Medium) - #209
# Longest Substring Without Repeating Characters (Medium) - #3
# Permutation in String (Medium) - #567
# Longest Repeating Character Replacement (Medium) - #424
# Find All Anagrams in a String (Medium) - #438

__________________________________________________________________________________


# Palindrome Number.py:
#Check if an integer 'x' reads the same forwards and backwards. Return true if it does, otherwise false. Negative numbers and numbers that change when reversed are not palindromes.

# Search Insert Position.py:
#The code defines a method searchInsert that uses binary search to find the index of a target in a sorted list nums. If the target exists, it returns its index. If not, it returns the index where the target should be inserted to maintain the order.
#Uses left, right, and mid pointers to search efficiently.
#If not found, left gives the correct insertion position.

# Roman to Integer.py:
#Convert a Roman numeral string into an integer by mapping each symbol to its value. Add values unless a smaller numeral comes before a larger one—then subtract. Supports standard Roman numeral rules and works for values from 1 to 3999.

# Remove Element.py:
#Remove all occurrences of a given value val from the array nums in-place. Rearrange the array so the first k elements are the ones not equal to val, and return k. The order of elements can change, and anything beyond the first k elements doesn't matter.

# Remove Duplicates From Sortey Array.py:
#Remove duplicates in a sorted integer array in-place so that each unique element appears only once. Return the number of unique elements, with the first part of the array holding these unique values in order.

# Longest Common Prefix.py:
#The code finds the longest common prefix by comparing characters of all strings one by one and trimming the prefix whenever a mismatch is found. It stops early if the prefix becomes empty.

#  Length Of Last Word.py:
#The code trims extra spaces and splits the string into words.It then returns the length of the last word in the resulting list.

# Find Index of First Occurrence in String.py:
#Given two strings, find the first position where the second string (needle) appears in the first string (haystack). Return that index, or -1 if it doesn’t appear.


