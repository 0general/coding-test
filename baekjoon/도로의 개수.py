"""
https://www.acmicpc.net/problem/1577
"""
from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dp = [[0]*(M+1) for _ in range(N+1)]
dp[0][0] = 1
dir = [(-1, 0), (0, -1)]
k = int(input())
check = defaultdict(list)
for _ in range(k):
    a, b, c, d = map(int, input().split())
    temp = [(a, b), (c, d)]
    temp.sort(key=lambda x: (x[0], x[1]))
    check[temp[1]].append(temp[0])

for i in range(N+1):
    for j in range(M+1):
        for d in dir:
            x, y = i+d[0], j+d[1]
            if x < 0 or y < 0:
                continue
            if (x, y) in check[(i, j)]:
                continue
            dp[i][j] += dp[x][y]

print(dp[N][M])
