"""
# Remove Duplicates from Sorted Array II

- **ID:** 80
- **Difficulty:** MEDIUM
- **Topic Tags:** Array, Two Pointers
- **Link:** [LeetCode Problem](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/)
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        have_seen_n_times = 0
        for x in nums:
            if x != nums[k]:
                k += 2 if have_seen_n_times > 1 else 1
                have_seen_n_times = 1
            else:
                have_seen_n_times += 1
            temp = k
            if have_seen_n_times > 1:
                temp = k + 1
            nums[temp] = x
        return k + 2 if have_seen_n_times > 1 else k + 1