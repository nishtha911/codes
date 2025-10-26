def is_safe(board, row, col, n):
    for i in range(col):  
        if board[row][i] == 1:
            return False
    for i,j in zip(range(row,-1,-1), range(col,-1,-1)):  
        if board[i][j] == 1:
            return False
    for i,j in zip(range(row,n), range(col,-1,-1)):  
        if board[i][j] == 1:
            return False
    return True

def print_board(board, n, solution_number):
    print(f"Solution {solution_number}:")
    for row in board:
        line = ['Q' if x == 1 else '.' for x in row]
        print("[", " ".join(line), "]")
    print()

def solve_nqueens(board, col, n, solution_number):
    if col >= n:
        solution_number[0] += 1  
        print_board(board, n, solution_number[0])
        return True
    
    res = False
    for i in range(n):
        if is_safe(board, i, col, n):  
            board[i][col] = 1  
            res = solve_nqueens(board, col + 1, n, solution_number) or res
            board[i][col] = 0  
    return res

n = 4  
board = [[0]*n for _ in range(n)]
solution_number = [0] 
print("N-Queens Problem Solutions (using Backtracking + Branch & Bound):\n")
solve_nqueens(board, 0, n, solution_number)


