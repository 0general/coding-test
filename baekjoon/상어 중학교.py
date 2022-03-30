"""
https://www.acmicpc.net/problem/21609
"""
import sys

from collections import deque


input = sys.stdin.readline


def bfs():
    global board, N, score, over
    q = deque()
    group = []
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if len(q) == 0 and not visited[i][j] and 1 <= board[i][j] <= M: # 기준 블록이면
                rainbow = []
                count = 1
                visited[i][j] = True
                v = board[i][j]
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    for d in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                        nx, ny = x+d[0], y+d[1]
                        if nx < 0 or nx >= N or ny < 0 or ny >= N:
                            continue
                        if not visited[nx][ny] and (board[nx][ny] == v or board[nx][ny] == 0):
                            visited[nx][ny] = True
                            count += 1
                            q.append((nx, ny))
                            if board[nx][ny] == 0:
                                rainbow.append((nx, ny))
                if count > 1:
                    group.append((count, len(rainbow), i, j))
                while rainbow: #무지개는 중복해서 세줘야 한다
                    x, y = rainbow.pop()
                    visited[x][y] = False
    if len(group) == 0: # 오토 플레이 종료 조건
        over = True
        return
    group.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3])) # 그룸 크기, 무지개 블록 수, 기준 블록 행, 기준 블록 열
    score += group[0][0]**2
    visited = [[False]*N for _ in range(N)]
    i, j = group[0][2], group[0][3]
    visited[i][j] = True
    q.append((i, j))
    v = board[i][j]
    board[i][j] = -2
    while q:
        x, y = q.popleft()
        for d in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx, ny = x+d[0], y+d[1]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if not visited[nx][ny] and (board[nx][ny] == v or board[nx][ny] == 0):
                visited[nx][ny] = True
                board[nx][ny] = -2
                q.append((nx, ny))
    return


def gravity():
    global board, N

    for j in range(N):
        top = N-1
        for i in range(N-1, -1, -1):
            if board[i][j] == -2:
                continue
            if board[i][j] == -1:
                top = i-1
            else:
                if top == i:
                    top -= 1
                    continue
                board[top][j] = board[i][j]
                top -= 1
                board[i][j] = -2


def rotate():
    global board, N
    for i in range(N//2+1):
        for j in range(i, N-1-i):
            board[i][j], board[N-1-j][i], board[N-1-i][N-1-j], board[j][N-1-i] \
                = board[j][N-1 - i], board[i][j], board[N-1-j][i], board[N-1-i][N-1-j]


over = False
score = 0
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

while not over:
    bfs()
    if over:
        break
    gravity()
    rotate()
    gravity()

print(score)
