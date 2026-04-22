"""
# H-Index

- **ID:** 274
- **Difficulty:** MEDIUM
- **Topic Tags:** Array, Sorting, Counting Sort
- **Link:** [LeetCode Problem](https://leetcode.com/problems/h-index/description/)

constraints:
length: [1,5000]
value: [0,1000]

[3,0,6,1,5]

[0,1,3,5,6]


[1,3,1]
[1,1,3,4,4,5,5,5,6,6]

at least h papers, each has at lease h citations
"""
from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        res = 0
        citations.sort()
        for i in range(n):
            res = max(res, min(citations[i], n - i))
        return res

class Solution2:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        count = [0]*(n+1)

        for x in citations:
            count[min(x, n)] += 1
        
        total = 0
        for h in range(n, -1, -1):
            total += count[h]
            if total >= h:
                return h
        return 0

test_cases = [
    [0],
    [1],
    [0,1],
    [1,2],
    [1,3,1],
    [3,0,6,1,5],
    [1,1,1,1,1],
    [0,0,0,0,0],
    [2,2,2,2,2],
    [3,3,3,3,3],
    [4,4,4,4,4],
    [5,5,5,5,5],
    [6,6,6,6,6]
]

sol = Solution2()
for test_case in test_cases:
    print(test_case, ": ", sol.hIndex(test_case))

# time complexity: O(nlog(n))
# space complexity: O(1)

# [3,0,6,1,5],
# [1,1,0,1,2]

