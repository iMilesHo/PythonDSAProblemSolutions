"""
# Roman to Integer

- **ID:** 13
- **Difficulty:** EASY
- **Topic Tags:** Hash Table, Math, String
- **Link:** [LeetCode Problem](https://leetcode.com/problems/roman-to-integer/description/)

## Problem Description:
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:

- I can be placed before V (5) and X (10) to make 4 and 9.
- X can be placed before L (50) and C (100) to make 40 and 90.
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

## Constraints:
- 1 <= s.length <= 15
- s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- It is guaranteed that s is a valid roman numeral in the range [1, 3999].

## Test Cases:
Input: s = "III"
Output: 3
Explanation: III = 3.

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V = 5, III = 3.

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
- I can be placed before V (5) and X (10) to make 4 and 9.
- X can be placed before L (50) and C (100) to make 40 and 90.
- C can be placed before D (500) and M (1000) to make 400 and 900.


test cases:
I       1 
II      2 
III     3 
IV      4 
V       5 
VI      6 
VII     7 
VIII    8 
IX      9 
X       10
XI      11
XII     12
XIII    13
XIV     14
LVIII   58
MCMXCIV 1994


I       1
II      2
III     3
X       10
XX      20
XXX     30
C       100
CC      200
CCC     300
M       1000
MM      2000
MMM     3000

IV      4
V       5
VI VII VIII      6,7,8

XL    40
L     50
LX LXX LXXX 60 70 80

CD      400
D       500
DC DCC DCCC 600 700 800
"""

class Solution:
    def __init__(self):
        self.dict = {
            "I" :       1,
            "II" :      2,
            "III" :     3,
            "IX" :      9,
            "X" :       10,
            "XX" :      20,
            "XXX" :     30,
            "XC" :      90,
            "C" :       100,
            "CC" :      200,
            "CCC" :     300,
            "CM" :      900,
            "M" :       1000,
            "MM" :      2000,
            "MMM" :     3000,
            "IV" :     4,
            "V" : 5,
            "XL": 40,
            "L": 50,
            "CD" : 400,
            "D" : 500
        }
    
    def romanToInt(self, s: str) -> int:
        i = 0
        n = len(s)
        total = 0
        while  i < n:
            if i + 2 < n and s[i:i+3] in self.dict:
                total += self.dict[s[i:i+3]]
                i += 3
            elif i + 1 < n and s[i:i+2] in self.dict:
                total += self.dict[s[i:i+2]]
                i += 2
            elif i < n and s[i] in self.dict:
                total += self.dict[s[i]]
                i += 1
            else:
                print("Error: Wrong Roman Charactor")
                return -1
        return total

class Solution2:
    def __init__(self):
        self.dict = {
            "I" :       1,
            "X" :       10,
            "C" :       100,
            "M" :       1000,
            "V" :       5,
            "L" :       50,
            "D" :       500
        }
    
    def romanToInt(self, s: str) -> int:
        i = 0
        n = len(s)
        total = 0
        while  i < n:
            if i + 1 < n and self.dict[s[i]] < self.dict[s[i+1]]:
                total += self.dict[s[i+1]] - self.dict[s[i]]
                i += 2
            else:
                total += self.dict[s[i]]
                i += 1
            
        return total


sol = Solution2()

test_cases = [
    "I",
    "II",
    "III",
    "LVIII",
    "MCMXCIV",
    "MCCLXXXIX"
]

for test_case in test_cases:
    print(test_case, " = ", sol.romanToInt(test_case))

