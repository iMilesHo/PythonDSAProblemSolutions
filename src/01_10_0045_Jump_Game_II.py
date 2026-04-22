"""
# Jump Game II

- **ID:** 45
- **Difficulty:** MEDIUM
- **Topic Tags:** Array, Dynamic Programming, Greedy
- **Link:** [LeetCode Problem](https://leetcode.com/problems/jump-game-ii/description/)
"""

from typing import List

class Solution:
    def dfs(self, nums: List[int], i: int, currSteps: int): # [2,3,1,1,4], 1, 1
        if i == (len(nums) - 1):
            if currSteps < self.miniSteps:
                self.miniSteps = currSteps
            return
        for j in range(1, nums[i]+1): # [1, 3)
            if (i + j) >  (len(nums) - 1) or currSteps + 1 >= self.miniSteps:
                break
            self.dfs(nums, i+j, currSteps + 1)

    def jump(self, nums: List[int]) -> int:
        self.miniSteps = float('inf')
        self.dfs(nums, 0, 0) # [2,3,1,1,4], 0, 0
        return self.miniSteps

class Solution2:
    def jump(self, nums: List[int]) -> int:
        fartest = 0
        n = len(nums)
        jump_times = 0
        for i in range(n):
            curr = i + nums[i]
            if curr <= fartest:
                return -1
            else:
                fartest = curr
                jump_times += 1
            if fartest == n - 1:
                break
                
        return jump_times

test_cases = [
    [0],
    [1],
    [1,0],
    [1,1,0],
    [2,3,1,1,4],
    [1,1,1,1,1],
    [1,1,1,1,0],
    [4,1,1,0,1],
    [2,0,4,1,0,0,2,0,1,0],
    [3,1,0,3,0,0,1,0]
]
sol = Solution()
for tc in test_cases:
    print(tc, " : ", sol.jump(tc))
