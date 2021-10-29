"""
https://www.acmicpc.net/problem/2206
"""
import sys
from collections import deque


def bfs():
    while q:
        (x, y), broken, cnt = q.popleft()
        if x == n-1 and y == m-1:
            return cnt
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and not visited[nx][ny][0]:
                    if broken and not visited[nx][ny][1]:
                        visited[nx][ny][1] = True
                        q.append(((nx, ny), True, cnt+1))
                    elif not broken and not visited[nx][ny][0]:
                        visited[nx][ny][0] = True
                        q.append(((nx, ny), False, cnt+1))
                if graph[nx][ny] == 1 and not broken and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    q.append(((nx, ny), True, cnt+1))
    return -1


input = sys.stdin.readline

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
q = deque()
n, m = map(int, input().split())
graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]
visited = [[[False, False] for _ in range(m)] for _ in range(n)]

visited[0][0][0] = True
q.append(((0, 0), False, 1))
print(bfs())
