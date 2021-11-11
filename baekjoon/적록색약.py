"""
https://www.acmicpc.net/problem/10026
"""
import sys


def rg_dfs(i, j):
    same = color[graph[i][j]]
    x, y = rg_stack.pop()
    for k in range(4):
        nx, ny = x+dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < N and not rg_visit[nx][ny] and color[graph[nx][ny]] == same:
            rg_visit[nx][ny] = True
            rg_stack.append((nx, ny))
            rg_dfs(nx, ny)


def dfs(i, j):
    x, y = stack.pop()
    for k in range(4):
        nx, ny = x+dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and graph[nx][ny] == graph[i][j]:
            visit[nx][ny] = True
            stack.append((nx, ny))
            dfs(nx, ny)


sys.setrecursionlimit(10000)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
color = {'R': 0, 'G': 0, 'B': 1}
input = sys.stdin.readline
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(input().rstrip()))

visit = [[False]*N for _ in range(N)]
rg_visit = [[False]*N for _ in range(N)]
stack = []
rg_stack = []
ans = [0, 0]
for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            ans[0] += 1
            visit[i][j] = True
            stack.append((i, j))
            dfs(i, j)
        if not rg_visit[i][j]:
            ans[1] += 1
            rg_visit[i][j] = True
            rg_stack.append((i, j))
            rg_dfs(i, j)

print(*ans)
