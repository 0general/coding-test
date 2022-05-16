"""
https://www.acmicpc.net/problem/17070
"""
import sys

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if (i == 0 and j == 0) or (i == 1 and j == 0) or arr[i][j]:
            continue
        if i == 0 and j == 1:
            dp[i][j] = [1, 0, 0]
            continue

        if 0 <= j-1 < N:
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]
        if 0 <= i-1 < N and 0 <= j-1 < N and not arr[i-1][j] and not arr[i][j-1]:
            dp[i][j][1] = sum(dp[i-1][j-1])
        if 0 <= i-1 < N:
            dp[i][j][2] = dp[i-1][j][1] + dp[i-1][j][2]

print(sum(dp[N-1][N-1]))
