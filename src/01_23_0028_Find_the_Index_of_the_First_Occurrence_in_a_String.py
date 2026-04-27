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


我能想到的KMP测试用例有：
aaaae
aabaaa
abcdabcdefgabcd
aaabaaaaaab
abcdddabcd
abcdefg

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

    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)

        # === 第一阶段：构建 lps 数组 ===
        lps = [0] * m
        length = 0  # 当前最长相等前后缀的长度
        i = 1
        while i < m:
            if needle[i] == needle[length]:
                # 能延伸
                length += 1
                lps[i] = length
                i += 1
            elif length > 0:
                # 不能延伸，但可以缩短（利用已有的lps信息）
                length = lps[length - 1]
                # 注意：i 不动
            else:
                # length==0 还不匹配，当前位置lps就是0
                lps[i] = 0
                i += 1

        # === 第二阶段：用 lps 加速匹配 ===
        p1 = p2 = 0
        while p1 < n:
            if haystack[p1] == needle[p2]:
                p1 += 1
                p2 += 1
            if p2 == m:
                return p1 - m          # 找到
            elif p1 < n and haystack[p1] != needle[p2]:
                if p2 > 0:
                    p2 = lps[p2 - 1]  # 利用lps跳转，p1不动
                else:
                    p1 += 1           # p2已经是0了，只能前进p1
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
