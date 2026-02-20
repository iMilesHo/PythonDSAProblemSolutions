"""
# Jump Game

- **ID:** 55
- **Difficulty:** MEDIUM
- **Topic Tags:** Array, Dynamic Programming, Greedy
- **Link:** [LeetCode Problem](https://leetcode.com/problems/jump-game/description/)

55. Jump Game
Medium
Topics
premium lock icon
Companies
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5

[0]
[1]
[1,0]
[0,1]
[1,1,1]
[0,0,0]
[6,0,0,0,0,0,0]
[5,0,0,0,0,0,0]
[3,1,0,3,0,0,1,0]
"""
from typing import List
class Solution:
    def depthFirstSearch(self, nums: List[int], index: int) -> bool: 
        if index >= len(nums) - 1:
            return True
        
        for i in range(1, nums[index] + 1):
            if self.depthFirstSearch(nums, index + i):
                return True
        return False

    def canJump(self, nums: List[int]) -> bool:
        return self.depthFirstSearch(nums, 0)
"""
time complexity: O(2^n) (each step has two options: skip or not skip, 2^(n-2))
space complexity: O(n) (the funtion call stack)
"""

class Solution:
    def depthFirstSearch(self, nums: List[int], index: int, canJumpRecord: List[int]) -> bool:
        if canJumpRecord[index] == 0:
            return False
        elif canJumpRecord[index] == 1:
            return True
        
        if index >= len(nums) - 1:
            return True
        
        for i in range(1, nums[index] + 1):
            if self.depthFirstSearch(nums, index + i,canJumpRecord):
                canJumpRecord[index] = 1
                return True
        canJumpRecord[index] = 0
        return False

    def canJump(self, nums: List[int]) -> bool:
        canJumpRecord = [-1]*len(nums) # -1:no record, 0: can't jump, 1: can jump
        return self.depthFirstSearch(nums, 0,canJumpRecord)
"""
this is actually a kind of DP (top down) (recursion + memoization)
time complexity: O(n*k) (k = max(nums[i]), we have space to replace time)
space complexity: O(n)
"""

class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        fartest = 0
        for i in range(len(nums)):
            if i > fartest:
                return False
            fartest = max(fartest, i + nums[i])
        return True
"""
greedy solution
time: O(n)
space:o(1)
"""

class Solution3:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False]*n
        
        for i in range(n-2, -1, -1):
            for j in range(1, nums[i] + 1):
                if i + j < n and dp[i + j]:
                    dp[i] = True
                    break
        return dp[0]

"""
DP (bottom-up)
time: O(n*k)
space:o(n)
"""

test_cases = [
    [0],
    [1],
    [1,0],
    [0,1],
    [1,1,0],
    [0,1,0],
    [2,3,1,1,4],
    [3,2,1,0,4],
    [1,1,1,1,1],
    [0,0,0,0,0],
    [1,1,1,0,1],
    [1,1,1,1,0],
    [4,1,1,0,1],
    [2,0,4,1,0,0,2,0,1,0],
    [3,1,0,3,0,0,1,0]
]
sol = Solution3()
for tc in test_cases:
    print(tc, " : ", sol.canJump(tc))


"""
Time complexity: O(n*max(nums[i]))
Space complexity: O(n)
"""