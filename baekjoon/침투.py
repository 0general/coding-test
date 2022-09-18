"""
https://www.acmicpc.net/problem/13565
"""
import sys
sys.setrecursionlimit(1000010)
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(M)]
visited = [[False for _ in range(N)] for _ in range(M)]
flag = False


def dfs(i, j):
    global flag
    if i == M-1:
        flag = True
        return
    for d in [(1, 0), (0, -1), (0, 1), (-1, 0)]:
        x, y = i + d[0], j + d[1]
        if x < 0 or y < 0 or x >= M or y >= N:
            continue
        if not visited[x][y] and arr[x][y] == '0':
            visited[x][y] = True
            dfs(x, y)
        if flag:
            return


for i in range(N):
    if not visited[0][i] and arr[0][i] == '0':
        visited[0][i] = True
        dfs(0, i)
    if flag:
        break

if flag:
    print('YES')
else:
    print('NO')
