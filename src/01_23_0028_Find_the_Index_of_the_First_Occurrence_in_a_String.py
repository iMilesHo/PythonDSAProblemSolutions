"""
# Find the Index of the First Occurrence in a String

- **ID:** 28
- **Difficulty:** EASY
- **Topic Tags:** Two Pointers, String, String Matching
- **Link:** [LeetCode Problem](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/)


aaaaaaaaae
aaaae


abcdefg
bcde
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        p1 = 0
        p2 = 0

        while p1 < len(haystack) and p2 < len(needle):
            if haystack[p1] == needle[p2]:
                p1 += 1
                p2 += 1
            else:
                p1 -= p2 - 1
                p2 = 0
            if p2 == len(needle):
                return p1 - len(needle)
        return -1
    
test_cases = [
    ["sadbutsad", "sad"],
    ["leetcode", "leeto"],
    ["abcdefghijk","bcde"],
    ["aaaaaaaaae", "aaaae"],
    ["a","a"],
    ["a","b"],
    ["a","bcd"],
    ["a","aaa"],
    ["abcabcabc","cab"],
    ["aaaae","aaae"]
]

sol = Solution()
for test_case in test_cases:
    print(sol.strStr(test_case[0], test_case[1]))
