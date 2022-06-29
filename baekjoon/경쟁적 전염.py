"""
https://www.acmicpc.net/problem/18405
"""
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
arr = []
virus = [deque() for _ in range(K+1)]
visited = [[False]*N for _ in range(N)]
for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(N):
        if arr[i][j] > 0:
            visited[i][j] = True
            virus[arr[i][j]].append((i, j))
S, X, Y = map(int, input().split())

dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for _ in range(S):
    for k in range(1, K+1):
        for _ in range(len(virus[k])):
            now = virus[k].popleft()
            for d in dir:
                nx, ny = now[0] + d[0], now[1] + d[1]
                if nx < 0 or ny < 0 or nx >= N or ny >= N or visited[nx][ny]:
                    continue
                visited[nx][ny] = True
                arr[nx][ny] = k
                virus[k].append((nx, ny))

print(arr[X-1][Y-1])
