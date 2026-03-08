"""八皇后问题求解器：在8x8棋盘上放置8个皇后，使其互不攻击"""

def is_safe(board, row, col, n=8):
    """
    检查当前位置(row, col)是否可以放置皇后
    :param board: 棋盘（二维列表）
    :param row: 当前行
    :param col: 当前列
    :param n: 棋盘大小（默认8）
    :return: 布尔值，是否安全
    """
    # 检查同一列
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # 检查左上到右下的对角线
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # 检查右上到左下的对角线
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens(n=8):
    """
    求解n皇后问题（默认8）
    :param n: 皇后数量/棋盘大小
    :return: 所有可行解（列表），每个解是二维列表表示的棋盘
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    
    def backtrack(row):
        if row == n:
            solutions.append([r.copy() for r in board])
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0
    
    backtrack(0)
    return solutions

if __name__ == "__main__":
    solutions = solve_n_queens(8)
    print(f"八皇后问题共有 {len(solutions)} 个解")
