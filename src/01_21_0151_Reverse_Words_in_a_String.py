"""
# Reverse Words in a String

- **ID:** 151
- **Difficulty:** MEDIUM
- **Topic Tags:** Two Pointers, String
- **Link:** [LeetCode Problem](https://leetcode.com/problems/reverse-words-in-a-string/description/)
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        sa = s.split()
        return " ".join(sa[::-1])

class Solution2:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        n = len(s)
        l, r = 0, n - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        i = 0
        while i < n:
            if s[i] == " ":
                i += 1
                continue
            l = i
            r = i
            while r+1 < n and s[r+1] != " ":
                r += 1
            i = r + 1
            while l < r: # 0 1 2 3 4
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        slow = 0
        fast = 0
        meet_word = True
        while fast < n:
            if s[fast] == ' ':
                fast += 1
                if meet_word and slow != 0:
                    s[slow] = " "
                    slow += 1
                meet_word = False
                continue
            meet_word = True
            s[slow] = s[fast]
            slow += 1
            fast += 1
        return "".join(s[:slow])

        
    
sol = Solution2()
print(sol.reverseWords("  the   sky   is   blue  "))
print(sol.reverseWords("  a   b   c   d  "))

