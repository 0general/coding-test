def solution(board):
    n, m = len(board), len(board[0])
    if n == 1 or m == 1:
        for i in range(n):
            for j in range(m):
                if board[i][j]:
                    return 1
    else:
        a = 0
        for i in range(1, n):
            for j in range(1, m):
                if board[i][j]:
                    mn = min(board[i-1][j], board[i][j-1], board[i-1][j-1])
                    board[i][j] = mn + 1
                    a = max(a, board[i][j])
                else:
                    continue
        if not a:
            if 1 in board[0]:
                return 1
            for i in range(n):
                if board[i][0]:
                    return 1
    return a**2
