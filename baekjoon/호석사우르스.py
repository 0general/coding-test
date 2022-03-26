"""
https://www.acmicpc.net/problem/22255
"""
import sys
import heapq
input = sys.stdin.readline
# 격자 크기
n, m = map(int, input().split())
MAX = 3*1e6 + 1
# 시작 지점, 끝 지점
sx, sy, ex, ey = map(int, input().split())
sx -= 1
sy -= 1
ex -= 1
ey -= 1
maps = [list(map(int, input().split())) for _ in range(n)]
dist = [[[MAX, MAX, MAX] for _ in range(m)] for _ in range(n)]
dx = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 우,상,좌,하
dist[0][0][1] = 0

h = []
heapq.heappush(h, (0, sx, sy, 1))
answer = MAX
while h:
    cost, x, y, cnt = heapq.heappop(h)
    if x == ex and y == ey:
        answer = min(answer, cost)
        continue
    if cnt == 0:  # 상하좌우 방향 모두
        for i in range(4):
            nx, ny = x+dx[i][0], y+dx[i][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or maps[nx][ny] == -1:
                continue
            d = cost + maps[nx][ny]
            if dist[nx][ny][1] <= d:
                continue
            dist[nx][ny][1] = d
            heapq.heappush(h, (d, nx, ny, 1))
    elif cnt == 1:  # 상하만
        for i in (1, 3):
            nx, ny = x+dx[i][0], y+dx[i][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or maps[nx][ny] == -1:
                continue
            d = cost + maps[nx][ny]
            if dist[nx][ny][2] <= d:
                continue
            dist[nx][ny][2] = d
            heapq.heappush(h, (d, nx, ny, 2))
    else:  # cnt = 2 다음엔 0으로 집어넣어야 한다.
        for i in (0, 2):
            nx, ny = x+dx[i][0], y+dx[i][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or maps[nx][ny] == -1:
                continue
            d = cost + maps[nx][ny]
            if dist[nx][ny][0] <= d:
                continue
            dist[nx][ny][0] = d
            heapq.heappush(h, (d, nx, ny, 0))

if answer == MAX:
    print(-1)
else:
    print(answer)
