"""
https://www.acmicpc.net/problem/2589
"""
import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    q = deque()
    visited[x][y] = 0
    q.append((x, y))
    while q:
        i, j = q.popleft()
        for k in range(4):
            nx, ny = i+dx[k], j+dy[k]
            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == -1 and graph[nx][ny] == 'L':
                visited[nx][ny] = visited[i][j] + 1
                q.append((nx, ny))
        if len(q) == 0:
            return visited[i][j]


'''
보물의 가로 세로 크기가 각각 50이하이다. -> 육지의 모든 point를 시작점으로 하여 최장거리를 찾아봐야 한다.
'''
h, w = map(int, input().split())
graph = []
land = []
for i in range(h):
    graph.append(list(input().rstrip()))
    for j in range(w):
        if graph[i][j] == 'L':
            land.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

long = -1

for lx, ly in land:
    visited = [[-1]*w for _ in range(h)]
    long = max(long, bfs(lx, ly))

print(long)
