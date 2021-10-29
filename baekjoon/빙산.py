"""
https://www.acmicpc.net/problem/2573
"""
import sys
from collections import deque

input = sys.stdin.readline


def melt(year):  # 상하좌우 0의 개수만큼 녹음
    minus = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                cnt = 0
                for k in range(len(dx)):
                    x, y = i+dx[k], j+dy[k]
                    if 0 <= x < n and 0 <= y < m and graph[x][y] == 0:
                        cnt += 1
                minus[i][j] = cnt

    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                graph[i][j] -= minus[i][j]
                if graph[i][j] < 0:
                    graph[i][j] = 0

    icelands = bfs()
    if icelands >= 2:
        return year
    elif icelands == 1:
        return melt(year+1)
    else:
        return 0


def bfs():  # 빙산 개수 체크
    visited = [[False]*m for _ in range(n)]
    cnt = 0
    q = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and not visited[i][j]:
                cnt += 1
                visited[i][j] = True
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    for k in range(len(dx)):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] != 0:
                            visited[nx][ny] = True
                            q.append((nx, ny))
    return cnt


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

print(melt(1))  # 한덩어리 빙산이 주어진다고 했으므로
