"""
# Longest Common Prefix

- **ID:** 14
- **Difficulty:** EASY
- **Topic Tags:** String, Trie
- **Link:** [LeetCode Problem](https://leetcode.com/problems/longest-common-prefix/description/)

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings


"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefixStr = ""
        n = len(strs[0])
        for i in range(n):
            temp = strs[0][i]
            for word in strs:
                if len(word) <= i:
                    return prefixStr
                if word[i] != temp:
                    return prefixStr
            prefixStr += temp
        return prefixStr

test_cases = [
    ["flower","flow","flight"],
    ["dog","racecar","car"],
    ["abcdefg", ""],
    [""],
    ["a","ab","abc"]
]

sol = Solution()
for test_case in test_cases:
    print(test_case, ": ", sol.longestCommonPrefix(test_case))
