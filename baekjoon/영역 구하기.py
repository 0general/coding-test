"""
https://www.acmicpc.net/problem/2583
"""
import sys
from collections import deque


def bfs():
    cnt = 1
    while q:
        nx, ny = q.popleft()
        for i in range(4):
            dx, dy = nx+dirx[i], ny+diry[i]
            if 0 <= dx < m and 0 <= dy < n and not visited[dx][dy]:
                visited[dx][dy] = True
                cnt += 1
                q.append((dx, dy))
    return cnt


input = sys.stdin.readline

# 평소에 쓰던 좌표평면과는 아래로 180도 뒤집어진 형태. 넓이에는 변함없음.
m, n, k = map(int, input().split())
visited = [[False]*n for _ in range(m)]
dirx = [0, 1, 0, -1]
diry = [1, 0, -1, 0]
ans = []

for _ in range(k):
    ly, lx, ry, rx = map(int, input().split())
    for i in range(lx, rx):
        for j in range(ly, ry):
            if not visited[i][j]:
                visited[i][j] = True

q = deque()
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            q.append((i, j))
            ans.append(bfs())

ans.sort()
print(len(ans))
print(*ans)
