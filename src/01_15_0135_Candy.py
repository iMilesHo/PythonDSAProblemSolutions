"""
# Candy

- **ID:** 135
- **Difficulty:** HARD
- **Topic Tags:** Array, Greedy
- **Link:** [LeetCode Problem](https://leetcode.com/problems/candy/description/)

contraints:
n == candy.length
1 <= n <= 2* 10^4
0 <= ratings[i] <= 2 * 10^4

[1,0,2]
output: 5
[2,1,2]

[1,2,2]
output:4
[1,2,1]

[1]

[1,1]

[1,2]

[2,1]

[1,1,1]

[2,1,1]

[1,2,1]

[1,1,2]

[1,2,2]

[2,1,2]

[2,2,1]

[1,1,1,1,1,1]

[1,1,2,1,1,2]

[1,2,1,2,1,2]

[1,2,3,4,5]

[1,2,3,4,5,1,2]
[1,2,3,4,5,1,2]

[5,4,3,2,1]

[1,2,3,4,5,1,2,3,4,5]
[1,1,1,1,1,1,1,1]
"""

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        res = [1]*n

        for i in range(n-1):
            if ratings[i] < ratings[i+1]:
                res[i+1] = res[i] + 1
        
        for i in range(n-1, 0, -1):
            if ratings[i] < ratings[i-1]:
                res[i-1] = max(res[i-1], res[i] + 1)
        
        print(res, end=", ")
        return sum(res)


test_cases = [
    [1],
    [1,1],
    [1,2],
    [2,1],
    [1,1,1],
    [2,1,1],
    [1,2,1],
    [1,1,2],
    [1,2,2],
    [2,1,2],
    [2,2,1],
    [1,1,1,1,1,1],
    [1,1,2,1,1,2],
    [1,2,1,2,1,2],
    [1,2,3,4,5],
    [5,4,3,2,1],
    [2,1,5,4,3],
    [1,2,3,4,5,1,2,3,4,5]
]

sol = Solution()

for test_case in test_cases:
    print(test_case, end=", ")
    res = sol.candy(test_case)
    print(res)


"""
# Notes: 找出可能的edges cases的技巧： 对于这种顺序不能变，前后大小对比很重要的，可以采用举如下的例子：
[1,2,3,4,5] + [1,2,3,4,5]
[5,4,3,2,1] + [5,4,3,2,1]
这种拼接方式可以拓展：
[1,2,3,4,5] + [5,4,3,2,1]
[5,4,3,2,1] + [1,2,3,4,5]

这样就可以模拟出周期函数里面的各个周期的振幅变化情况

这个题有两个传递关系，分别用两个loop计算，题眼是在从右到左的时候的那个max

这个题的分解首先发现了它有一个传递的过程，包括从左到右还有从右到左，如果是只去处理局部的话，很难处理
"""