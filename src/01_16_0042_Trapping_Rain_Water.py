"""
# Trapping Rain Water

- **ID:** 42
- **Difficulty:** HARD
- **Topic Tags:** Array, Two Pointers, Dynamic Programming, Stack, Monotonic Stack
- **Link:** [LeetCode Problem](https://leetcode.com/problems/trapping-rain-water/description/)

constraints:
n == height.lenght
1 <= n <= 2 * 10 ^ 4
0 <= height[i] <= 10^5

[0,1,0,2,1,0,1,3,2,1,2,1]
left_h:3
i:1
right_h:2
total:+1+1+2+1+1


[4,2,0,3,2,5]

[1]

[1,2]

[2,1]

[1,2,3]

[1,3,2]

[2,1,3]

[2,3,1]

[1,2,3,1,2,3]
[3,2,1,1,2,3]
[1,2,3,3,2,1]
[3,2,1,3,2,1]

[1,2,3,1,2,3,1,2,3]
"""

from typing import List

class Solution: # [0,1,0,2,1,0,1,3,2,1,2,1]
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lh_idx = 0 # left current highest
        rh_idx = n - 1 # right current highest
        i = 0
        total = 0

        i = lh_idx + 1 if height[lh_idx] <= height[rh_idx] else rh_idx - 1

        while lh_idx < rh_idx and i > lh_idx and i < rh_idx:
            lh = height[lh_idx]
            rh = height[rh_idx]
            min_h = min(lh,rh)
            if height[i] < min_h:
                total += min_h - height[i]
            
            if lh <= rh:
                if height[i] >= lh:
                    lh_idx = i
                    i = lh_idx + 1 if height[lh_idx] <= height[rh_idx] else rh_idx - 1
                    continue
                i += 1
            else:
                if height[i] >= rh:
                    rh_idx = i
                    i = lh_idx + 1 if height[lh_idx] <= height[rh_idx] else rh_idx - 1
                    continue
                i -= 1
        return total

            

if __name__ == "__main__":
    sol = Solution()
    print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))

"""
我先是考虑了局部的从左到右的方法，记录左边的最大值，发现我很难知道当前的点是不是应该算上，
所以这样的话，就得不停的回溯，状态永远不确定，而且这个题又不是那种，可以分解为二叉树那种可以回溯的问题。
后面回忆起来，可以尝试，双指针，记录左边和右边的最大值，然后从小的那个值的那边往中间探索，这个时候小的那边的状态就是确定的，
它可以盛的水也是确定的，就永远从小的那边开始往中间探索，遇到更高的局部最高值，就替换，然后重新判断哪边是小的那边
"""