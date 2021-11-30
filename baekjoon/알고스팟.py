"""
https://www.acmicpc.net/problem/1261
"""
import sys
from collections import deque


input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
m, n = map(int, input().split())
q = deque()
graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
find = False

visited[0][0] = True
q.append((0, 0))
while q:
    r, c = q.popleft()
    for i in range(len(dx)):
        nr, nc = r+dx[i], c+dy[i]
        if (0 <= nr < n) and (0 <= nc < m) and not visited[nr][nc]:
            visited[nr][nc] = True
            if graph[nr][nc] == 0:
                # 우선순위 큐를 사용해도 좋겠지만 그냥 단순히 0인 경우 바로 q의 앞에 넣어줘도 된다.
                q.appendleft((nr, nc))
            else:
                q.append((nr, nc))
            graph[nr][nc] += graph[r][c]
            if nr == n-1 and nc == m-1:
                find = True
                break
    if find:
        break

print(graph[n-1][m-1])
