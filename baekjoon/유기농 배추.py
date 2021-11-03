"""
https://www.acmicpc.net/problem/1012
"""
import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    stack = []
    cnt = 0
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    visit = [[False]*m for _ in range(n)]
    for _ in range(k):  # 그래프 갱신
        j, i = map(int, input().split())
        graph[i][j] = 1
    for u in range(n):
        for v in range(m):
            if graph[u][v] and not visit[u][v]:
                visit[u][v] = True
                cnt += 1
                stack.append((u, v))
                while stack:
                    x, y = stack[-1]
                    out = True
                    if 0 <= x-1 < n and not visit[x-1][y] and graph[x-1][y]:
                        visit[x-1][y] = True
                        stack.append((x-1, y))
                        out = False
                    if 0 <= x+1 < n and not visit[x+1][y] and graph[x+1][y]:
                        visit[x+1][y] = True
                        stack.append((x+1, y))
                        out = False
                    if 0 <= y+1 < m and not visit[x][y+1] and graph[x][y+1]:
                        visit[x][y+1] = True
                        stack.append((x, y+1))
                        out = False
                    if 0 <= y-1 < m and not visit[x][y-1] and graph[x][y-1]:
                        visit[x][y-1] = True
                        stack.append((x, y-1))
                        out = False
                    if out:
                        stack.pop()
    print(cnt)
