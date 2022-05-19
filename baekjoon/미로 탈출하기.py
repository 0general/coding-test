"""
https://www.acmicpc.net/problem/17090
"""
import sys

input = sys.stdin.readline
sys.setrecursionlimit(250010)

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

visited = [[False]*M for _ in range(N)]
ok = [[0]*M for _ in range(N)]

num = 0


def check(i, j):
    if visited[i][j]:
        return ok[i][j]
    visited[i][j] = True
    x, y = i, j
    if arr[i][j] == 'U':
        x -= 1
    elif arr[i][j] == 'R':
        y += 1
    elif arr[i][j] == 'D':
        x += 1
    else:
        y -= 1
    if x < 0 or y < 0 or x >= N or y >= M:
        ok[i][j] = 1
    else:
        ok[i][j] = check(x, y)
    return ok[i][j]


for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            check(i, j)
        num += ok[i][j]

print(num)
