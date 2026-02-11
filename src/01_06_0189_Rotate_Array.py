"""
# Rotate Array

- **ID:** 189
- **Difficulty:** MEDIUM
- **Topic Tags:** Array, Math, Two Pointers
- **Link:** [LeetCode Problem](https://leetcode.com/problems/rotate-array/description/)


Constraints:

1 <= nums.length <= 10^5
-231 <= nums[i] <= 2^31 - 1
0 <= k <= 10^5

[1] k = 0,1,2,3,4
[1,2]
[1,2,3]
[1,2,3,4]
[1,2,3,4,5]
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        # edges cases
        if k == 0:
            return 

        # rotate the whole array
        l, r = 0, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1 

        # rotate the first k
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1 

        # rotate the rest
        l, r = k, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1 