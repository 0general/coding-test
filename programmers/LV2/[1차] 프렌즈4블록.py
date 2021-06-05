def square(m, n, block):
    stack = set([])
    for i in range(n-1):
        for j in range(m-1):
            if block[i][j] != "_" and len(set([block[i][j], block[i+1][j], block[i][j+1], block[i+1][j+1]])) == 1:
                stack.update([(i, j), (i+1, j), (i, j+1), (i+1, j+1)])
    return list(stack)


def remove(m, n, block, answer):
    stack = square(m, n, block)
    if len(stack) == 0:
        return answer, block, False

    for k in stack:
        block[k[0]][k[1]] = "_"
    answer += len(stack)

    for i in range(len(block)):
        rline = []
        aline = []
        for j in range(m):
            if block[i][j] == "_":
                rline.append("_")
            else:
                aline.append(block[i][j])
        rline.extend(aline)
        block[i] = rline

    return answer, block, True


def solution(m, n, board):
    board = list(map(list, board))
    block = [[board[j][i] for j in range(m)]for i in range(n)]
    answer = 0
    while True:
        answer, block, Out = remove(m, n, block, answer)
        if not Out:
            break

    return answer
