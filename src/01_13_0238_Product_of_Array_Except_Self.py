"""
# Product of Array Except Self

- **ID:** 238
- **Difficulty:** MEDIUM
- **Topic Tags:** Array, Prefix Sum
- **Link:** [LeetCode Problem](https://leetcode.com/problems/product-of-array-except-self/description/)

Given an integer array nums, return an array answer such that answer[i] is equal
to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Constraints:
2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity?
(The output array does not count as extra space for space complexity analysis.)

Example 1:
Input:  nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input:  nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


[1,2,3,4]

[1,1,2,6]
[24,12,4,1]
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = 1
        suffix = 1
        res = [1]*n
        for i in range(n):
            res[i] *= prefix
            prefix = nums[i] * prefix

            res[n-i-1] *= suffix
            suffix = nums[n-i-1] * suffix
        
        return res


# --- Testing ---
if __name__ == "__main__":
    s = Solution()

    # Example 1
    assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6], "Example 1 failed"

    # Example 2
    assert s.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0], "Example 2 failed"

    # Example 2
    assert s.productExceptSelf([0,0,0]) == [0, 0, 0], "Example 3 failed"

    print("All tests passed!")





