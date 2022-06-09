"""
https://www.acmicpc.net/problem/2638
"""
import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
h = []
board = [list(map(int, input().split())) for _ in range(N)]
arr = [[[0, 0, 0, 0] for _ in range(M)] for _ in range(N)]
visited = [[False]*M for _ in range(N)]
dir = [(1, 0), (0, 1), (0, -1), (-1, 0)]
day = 0

visited[0][0] = True
heapq.heappush(h, (0, 0, 0))

while h:
    d, x, y = heapq.heappop(h)
    if day < d:
        day = d

    for k in range(4):
        nx, ny = x + dir[k][0], y + dir[k][1]
        if nx < 0 or ny < 0 or nx >= N or ny >= M or visited[nx][ny] or arr[nx][ny][k]:
            continue
        if board[nx][ny] == 0:
            visited[nx][ny] = True
            heapq.heappush(h, (d, nx, ny))
            continue
        arr[nx][ny][k] = 1
        if sum(arr[nx][ny]) >= 2:
            visited[nx][ny] = True
            heapq.heappush(h, (d+1, nx, ny))

print(day)
