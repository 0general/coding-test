"""
https://www.acmicpc.net/problem/16946
"""
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(n):
    for j in range(m):
        if arr[i][j] or visited[i][j]:
            continue
        q = deque()
        s = set()
        visited[i][j] = True
        q.append((i, j))
        num = 0
        while q:
            x, y = q.popleft()
            num = (num+1) % 10
            for d in dir:
                nx, ny = x + d[0], y + d[1]
                if nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny]:
                    continue
                if arr[nx][ny]:
                    s.add((nx, ny))
                    continue
                visited[nx][ny] = True
                q.append((nx, ny))
        while s:
            x, y = s.pop()
            arr[x][y] += num

for i in range(n):
    for j in range(m):
        print(arr[i][j] % 10, end='')
    print()
