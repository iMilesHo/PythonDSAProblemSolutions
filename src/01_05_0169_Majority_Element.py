"""
# Majority Element

- **ID:** 169
- **Difficulty:** EASY
- **Topic Tags:** Array, Hash Table, Divide and Conquer, Sorting, Counting
- **Link:** [LeetCode Problem](https://leetcode.com/problems/majority-element/description/)

[3,2,3]
candidate = 3
have_seen_n_times = 1
"""
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        have_seen_n_times = 0
        for x in nums: # Boyer-Moore 算法
            if x == candidate:
                have_seen_n_times += 1
            else:
                have_seen_n_times -= 1
                if have_seen_n_times == -1:
                    candidate = x
                    have_seen_n_times = 1
        return candidate

class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 0
        for x in nums:
            if count == 0:
                candidate = x
            count += 1 if x == candidate else -1
        return candidate

"""
Elevator pitch:

"""