from typing import List


def isValid(board: List[List[str]], row: int, col: int, val: str) -> bool:
    """检查在 board[row][col] 填入 val 是否合法"""

    # 1) 检查同一行有没有重复
    for j in range(9):
        if board[row][j] == val:
            return False

    # 2) 检查同一列有没有重复
    for i in range(9):
        if board[i][col] == val:
            return False

    # 3) 检查所在的 3x3 小方块有没有重复
    start_row = (row // 3) * 3  # 小方块左上角的行
    start_col = (col // 3) * 3  # 小方块左上角的列
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == val:
                return False

    return True  # 三项检查都通过，可以填！


def sudoku_solve(board: List[List[str]]) -> bool:
    """用回溯法解数独：找空格 → 试数字 → 递归 → 不行就擦掉"""
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":            # 找到一个空格
                for val in "123456789":       # 依次尝试 1~9
                    if isValid(board, i, j, val):  # 合法吗？
                        board[i][j] = val          # 填上
                        if sudoku_solve(board):    # 递归去解下一个空格
                            return True            # 全部解完！
                        board[i][j] = "."          # 走不通，擦掉（回溯）
                return False  # 1~9 都试过了都不行 → 前面某步填错了
    return True  # 没有空格了 → 解完了！

  
# debug your code below
board = [
    [".", ".", ".", "7", ".", ".", "3", ".", "1"],
    ["3", ".", ".", "9", ".", ".", ".", ".", "."],
    [".", "4", ".", "3", "1", ".", "2", ".", "."],
    [".", "6", ".", "4", ".", ".", "5", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "1", ".", ".", "8", ".", "4", "."],
    [".", ".", "6", ".", "2", "1", ".", "5", "."],
    [".", ".", ".", ".", ".", "9", ".", ".", "8"],
    ["8", ".", "5", ".", ".", "4", ".", ".", "."]
]

print(sudoku_solve(board))