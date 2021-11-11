"""
https://www.acmicpc.net/problem/21922
"""
import sys
from collections import deque


def bfs():
    global cnt
    while q:
        x, y, i = q.popleft()  # 행, 열, 바람 방향
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny][i]:
            if not visited[nx][ny]:
                visited[nx][ny] = 1
                cnt += 1
            visit[nx][ny][i] = True
            visit[nx][ny][i ^ 2] = True
            node = graph[nx][ny]
            if node == 0:
                pass
            elif node == 1 and i % 2 == 0:
                i ^= 2
            elif node == 2 and i % 2 == 1:
                i = 4-i
            elif node == 3:
                i ^= 3
            elif node == 4:
                i ^= 1
            q.append((nx, ny, i))


# 이동방향 0: 오른쪽, 1:아래쪽, 2:왼쪽, 3: 위쪽
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
q = deque()
for i in range(n):
    graph.append(list(map(int, input().rstrip().split())))

visited = [[0]*m for _ in range(n)]
# 바람이 들어오는 방향에 따라 visit
visit = [[[False]*4 for _ in range(m)] for _ in range(n)]
cnt = 0  # 원하는 자리 수

for i in range(n):
    for j in range(m):
        if graph[i][j] == 9:
            visit[i][j] = [True, True, True, True]
            visited[i][j] = 1
            cnt += 1
            for k in range(4):  # 전해지는 i 방향의 바람
                q.append((i, j, k))

bfs()
print(cnt)
