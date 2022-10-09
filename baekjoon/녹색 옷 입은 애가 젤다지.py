"""
https://www.acmicpc.net/problem/4485
"""
import sys
import heapq

input = sys.stdin.readline

idx = 1
MAX = 150000
while True:
    n = int(input())
    if n == 0:
        break
    dp = [[MAX for _ in range(n)] for _ in range(n)]
    arr = [list(map(int, input().split())) for _ in range(n)]
    h = []
    dp[0][0] = arr[0][0]
    heapq.heappush(h, (arr[0][0], 0, 0))

    while h:
        c, i, j = heapq.heappop(h)
        if i == n-1 and j == n-1:
            break
        if c > dp[i][j]:
            continue
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            x, y = i + dx, j + dy
            if x < 0 or y < 0 or x >= n or y >= n:
                continue
            cost = dp[i][j] + arr[x][y]
            if cost < dp[x][y]:
                dp[x][y] = cost
                heapq.heappush(h, (cost, x, y))
    print(f"Problem {idx}: {dp[n-1][n-1]}")
    idx += 1
