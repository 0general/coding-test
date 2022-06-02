"""
https://www.acmicpc.net/problem/2636
"""
import sys
import heapq

input = sys.stdin.readline

day = 0
num = 0

r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
visited = [[False]*c for _ in range(r)]

visited[0][0] = True
h = []
heapq.heappush(h, (0, 0, 0))

while h:
    d, i, j = heapq.heappop(h)
    if d != 0 and day == d and arr[i][j]:
        num += 1
    elif d > day:
        day = d
        num = 1

    for k in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        x, y = i + k[0], j + k[1]
        if x < 0 or y < 0 or x >= r or y >= c or visited[x][y]:
            continue
        visited[x][y] = True
        if arr[x][y] == 0:
            heapq.heappush(h, (d, x, y))
        else:
            heapq.heappush(h, (d+1, x, y))

print(day)
print(num)
