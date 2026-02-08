"""
# Merge Sorted Array

- **ID:** 88
- **Difficulty:** EASY
- **Topic Tags:** Array, Two Pointers, Sorting
- **Link:** [LeetCode Problem](https://leetcode.com/problems/merge-sorted-array/description/)

Constraints:
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]


"""

class Solution:
    # nums1 = [0], m = 0, nums2 = [1], n = 1
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2, p = m - 1, n - 1, m + n - 1
        if n == 0:
            return
        
        while p2 >= 0 : # p2 = 0
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

"""
elevator pitch
> “I merge **in‑place, from the back**.
> Three indices: `i = m‑1`, `j = n‑1`, `k = m+n‑1`.
> While `j ≥ 0`, write the larger of `nums1[i]` and `nums2[j]` to `nums1[k]`, moving the corresponding pointer left.
"""