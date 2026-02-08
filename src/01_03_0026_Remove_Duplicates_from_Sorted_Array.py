"""
# Remove Duplicates from Sorted Array

- **ID:** 26
- **Difficulty:** EASY
- **Topic Tags:** Array, Two Pointers
- **Link:** [LeetCode Problem](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)


[1,1,2]
k = 0
x_index = 2

"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for x in nums:
            if x != nums[k]:
                k += 1
            nums[k] = x
            
        return k + 1