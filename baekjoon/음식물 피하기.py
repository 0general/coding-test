"""
https://www.acmicpc.net/problem/1743
"""
import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [[0 for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    arr[r][c] = 1

dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

MAX = 0
q = deque()
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue
        visited[i][j] = True
        if arr[i][j] == 0:
            continue
        q.append((i, j))
        temp = 0
        while q:
            x, y = q.popleft()
            temp += 1
            for d in dir:
                nx, ny = x + d[0], y + d[1]
                if nx < 0 or ny < 0 or nx >= N or ny >= M or visited[nx][ny]:
                    continue
                visited[nx][ny] = True
                if arr[nx][ny]:
                    q.append((nx, ny))
        MAX = max(MAX, temp)

print(MAX)
