"""
# Integer to Roman

- **ID:** 12
- **Difficulty:** MEDIUM
- **Topic Tags:** Hash Table, Math, String
- **Link:** [LeetCode Problem](https://leetcode.com/problems/integer-to-roman/description/)

1       I
2       II
3       III
4       IV
5       V
6       VI
7       VII
8       VIII
9       IX
10      X
20      XX
30      XXX
40      XL
50      L
60      LX
70      LXX
80      LXXX
90      XC
100     C
200     CC
300     CCC
400     CD
500     D
600     DC
700     DCC
800     DCCC
900     CM
1000    M
2000    MM
3000    MMM

1,2,3,4,5,6,7,8,9,10,58,1994,1289
[1000,900,90,4]
[M,CM,XC,I]
"""

class Solution:
    def __init__(self):
        self.dict = {
            "1" :       "I",
            "2" :       "II",
            "3" :       "III",
            "4" :       "IV",
            "5" :       "V",
            "6" :       "VI",
            "7" :       "VII",
            "8" :       "VIII",
            "9" :       "IX",
            "10" :      "X",
            "20" :      "XX",
            "30" :      "XXX",
            "40" :      "XL",
            "50" :      "L",
            "60" :      "LX",
            "70" :      "LXX",
            "80" :      "LXXX",
            "90" :      "XC",
            "100" :     "C",
            "200" :     "CC",
            "300" :     "CCC",
            "400" :     "CD",
            "500" :     "D",
            "600" :     "DC",
            "700" :     "DCC",
            "800" :     "DCCC",
            "900" :     "CM",
            "1000" :    "M",
            "2000" :    "MM",
            "3000" :    "MMM"
        }
    # 1289
    def intToRoman(self, number: int) -> str:
        number_str = f"{number}"
        n = len(number_str)
        i = n - 1
        res = ""
        while i >= 0:
            if f"{int(number_str[i])*pow(10,n-i-1)}" in self.dict:
                res = self.dict[f"{int(number_str[i])*pow(10,n-i-1)}"] + res
                i -= 1
            else:
                return "Error"
        return res

class Solution2:
    def intToRoman(self, num: int) -> str:
        val_sym = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
            (1, "I")
        ]
        res = ""
        for val, sym in val_sym:
            while num >= val:
                res += sym
                num -= val
        return res


sol = Solution2()
test = 1994
print(test, "=", sol.intToRoman(test))

test_cases = [
    1,2,3,4,5,6,7,8,9,1994,1289,3999
]

for test_case in test_cases:
    print(test_case, "=", sol.intToRoman(test_case))