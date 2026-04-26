"""
# Zigzag Conversion

- **ID:** 6
- **Difficulty:** MEDIUM
- **Topic Tags:** String
- **Link:** [LeetCode Problem](https://leetcode.com/problems/zigzag-conversion/description/)
PAYPALISHIRING row = 4
P     I    N
A   L S  I G
Y A   H R
P     I

14/(4+4-2)
len(s)/(2*numRows-2) + 1

row = 3
P   A   H   N
A P L S I I G
Y   I   R

row = 5
P   H
A  SI
Y I R
PL  IG
A   N 
PHASIYIRPLIGAN
"""


class Solution:
    def printTable(self, table, numRows, s):
        for i in range(numRows):
            for j in range(len(s)):
                print(table[i][j], end=" ")
            print()

    def convert(self, s: str, numRows: int) -> str:
        table = [[" " for _ in range(len(s))] for _ in range(numRows)]
        j = 0
        k = 0
        while k < len(s):
            # Zig
            for i in range(numRows):
                if k >= len(s):
                    break
                table[i][j] = s[k]
                k += 1
            if k >= len(s):
                    break
            # Zag
            j += 1
            for i in range(numRows-2,0,-1):
                if k >= len(s):
                    break
                table[i][j] = s[k]
                j += 1
                k += 1
        # self.printTable(table,numRows,s)
        res = ""
        for i in range(numRows):
            for col in range(j+1):
                if table[i][col] != " ":
                    res += table[i][col]
        return res
    def convert1(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        table = ['']*numRows
        i = 0
        while i < len(s):
            for j in range(numRows):
                if i >= len(s):
                    break
                table[j] += s[i]
                i += 1
            if i >= len(s):
                    break
            
            for j in range(numRows-2,0,-1):
                if i >= len(s):
                    break
                table[j] += s[i]
                i += 1
        return "".join(table)



    def convert2(self, s: str, numRows: int) -> str:
      if numRows == 1 or numRows >= len(s):
          return s

      p = 2 * numRows - 2
      res = []

      for i in range(numRows):
          j = 0
          while j * p + i < len(s):
              res.append(s[j * p + i])            # 每周期第一个字符
              if 0 < i < numRows - 1:             # 中间行有第二个字符
                  idx2 = (j + 1) * p - i
                  if idx2 < len(s):
                      res.append(s[idx2])
              j += 1

      return ''.join(res)

"""
Time complexity: O(numRows*len(s))
"""


test_cases = [
    "PAYPALISHIRING",
    "PAYPALISHIRING",
    "PAYPALISHIRING",
    "A"
]

numRowss = [
    3,4,5,1
]

expected_results = [
    "PAHNAPLSIIGYIR",
    "PINALSIGYAHRPI",
    "PHASIYIRPLIGAN",
    "A"
]

sol = Solution()
for i in range(len(test_cases)):
    print(sol.convert1(test_cases[i], numRowss[i])==expected_results[i])

        