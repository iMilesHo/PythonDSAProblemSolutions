"""
# Length of Last Word

- **ID:** 58
- **Difficulty:** EASY
- **Topic Tags:** String
- **Link:** [LeetCode Problem](https://leetcode.com/problems/length-of-last-word/description/)

test cases:
Input: s = "Hello World"
Output: 5

Input: s = "   fly me   to   the moon  "
Output: 4

Input: s = "luffy is still joyboy"
Output: 6

"a"

"a b "
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        res = 0
        haveSeen = False
        for i in range(n-1,-1,-1):
            if not haveSeen and s[i] == " ":
                continue
            elif s[i] != " ":
                haveSeen = True
                res += 1
            elif s[i] == " ":
                return res
        return res
                

test_cases = [
    "Hello World",
    "   fly me   to   the moon  ",
    "luffy is still joyboy",
    "a",
    "a b "
]

sol = Solution()
for test_case in test_cases:
    print(test_case, ": ", sol.lengthOfLastWord(test_case))