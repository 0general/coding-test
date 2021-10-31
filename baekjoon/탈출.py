"""
https://www.acmicpc.net/problem/3055
"""
import sys
from collections import deque


def bfs():
    nw = len(water)
    nq = len(q)
    while nw or nq:
        for i in range(nw):
            x, y = water.popleft()
            for j in range(len(dx)):
                nx, ny = x + dx[j], y + dy[j]
                if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in {"D", "X"} and not visited[nx][ny]:
                    visited[nx][ny] = True
                    graph[nx][ny] = "*"
                    water.append((nx, ny))
        for i in range(nq):
            x, y, cnt = q.popleft()
            if graph[x][y] == "*":
                continue
            for j in range(len(dx)):
                nx, ny = x + dx[j], y + dy[j]
                if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in {"*", "X"} and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if graph[nx][ny] == "D":
                        print(cnt + 1)
                        return
                    q.append((nx, ny, cnt+1))
        nw = len(water)
        nq = len(q)
    print("KAKTUS")
    return


input = sys.stdin.readline

r, c = map(int, input().split())
graph = []
water = deque()
q = deque()
visited = [[False]*c for _ in range(r)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(r):
    graph.append(list(input().rstrip()))
    for j in range(c):
        if graph[i][j] == "*":
            visited[i][j] = True
            water.append((i, j))
        elif graph[i][j] == "S":
            visited[i][j] = True
            q.append((i, j, 0))

bfs()
