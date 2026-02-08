"""
# Remove Element

- **ID:** 27
- **Difficulty:** EASY
- **Topic Tags:** Array, Two Pointers
- **Link:** [LeetCode Problem](https://leetcode.com/problems/remove-element/description/)

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]


[1,1,1,1,1,1,1] 2
"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for x in nums:
            nums[k] = x
            if x != val:
                k += 1
        return k
    
"""
Elevator Pitch:
I use a single pointer `k` to track the position of the next non-`val` element. When I encounter an element not equal to `val`, I place it at index `k` and increment `k`. Finally, `k` represents the new length of the array without `val`.
"""