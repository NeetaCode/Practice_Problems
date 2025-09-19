# PROBLEM STATEMENT:
# Time Planner
# Implement a function meetingPlanner that given the availability, slotsA and slotsB, of two people and a meeting duration dur, returns the earliest time slot that works for both of them and is of duration dur. If there is no common time slot that satisfies the duration requirement, return an empty array.

# Time is given in a Unix format called Epoch, which is a nonnegative integer holding the number of seconds that have elapsed since 00:00:00 UTC, Thursday, 1 January 1970.

# Each person’s availability is represented by an array of pairs. Each pair is an epoch array of size two. The first epoch in a pair represents the start time of a slot. The second epoch is the end time of that slot. The input variable dur is a positive integer that represents the duration of a meeting in seconds. The output is also a pair represented by an epoch array of size two.

# In your implementation assume that the time slots in a person’s availability are disjointed, i.e, time slots in a person’s availability don’t overlap. Further assume that the slots are sorted by slots’ start time.

# Implement an efficient solution and analyze its time and space complexities.

# Examples:

# input:  slotsA = [[10, 50], [60, 120], [140, 210]]
#         slotsB = [[0, 15], [60, 70]]
#         dur = 8
# output: [60, 68]

# input:  slotsA = [[10, 50], [60, 120], [140, 210]]
#         slotsB = [[0, 15], [60, 70]]
#         dur = 12
# output: [] # since there is no common slot whose duration is 12
# Constraints:

# [time limit] 5000ms

# [input] array.array.integer slotsA

# 1 ≤ slotsA.length ≤ 100
# slotsA[i].length = 2
# [input] array.array.integer slotsB

# 1 ≤ slotsB.length ≤ 100
# slotsB[i].length = 2
# [input] integer


from typing import List

def meeting_planner(slotsA: List[List[int]], slotsB: List[List[int]], dur: int) -> List[int]:
    i, j = 0, 0

    while i < len(slotsA) and j < len(slotsB):
        # Find the overlap between current slots
        start = max(slotsA[i][0], slotsB[j][0])
        end = min(slotsA[i][1], slotsB[j][1])

        # If overlap is enough for meeting duration
        if end - start >= dur:
            return [start, start + dur]

        # Move the pointer that ends earlier
        if slotsA[i][1] < slotsB[j][1]:
            i += 1
        else:
            j += 1

    return []


# Example tests
print(meeting_planner(
    [[10, 50], [60, 120], [140, 210]],
    [[0, 15], [60, 70]],
    8
))  # Output: [60, 68]

print(meeting_planner(
    [[10, 50], [60, 120], [140, 210]],
    [[0, 15], [60, 70]],
    12
))  # Output: []


[output] array.integer


# Performance Feedback

# Current Performance: 2/10

# Target: 5/10 (with optimization and practice)

# Notes:

# Easy-level problems solvable without debugging

# Focus areas:

# Arrays & Strings

# Sorting & Searching

# Binary Search, BST, Binary Tree

# Graphs & Heaps

# Greedy Algorithms

# Dynamic Programming
