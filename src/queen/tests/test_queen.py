"""八皇后求解器单元测试"""
import pytest
from src.queen.solver import is_safe, solve_n_queens

def test_is_safe():
    board = [[0]*8 for _ in range(8)]
    board[0][0] = 1
    assert is_safe(board, 0, 0) is False
    assert is_safe(board, 1, 0) is False
    assert is_safe(board, 1, 1) is False
    assert is_safe(board, 1, 2) is True

def test_solve_n_queens_8():
    solutions = solve_n_queens(8)
    assert len(solutions) == 92
    first_sol = solutions[0]
    for row in first_sol:
        assert sum(row) == 1
    for col in range(8):
        assert sum(r[col] for r in first_sol) == 1

def test_solve_n_queens_4():
    solutions = solve_n_queens(4)
    assert len(solutions) == 2
