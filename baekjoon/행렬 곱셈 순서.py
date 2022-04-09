"""
https://www.acmicpc.net/problem/11049
"""
import sys

input = sys.stdin.readline

N = int(input())
diag = [list(map(int, input().split())) for _ in range(N)]
dp = [[2 << 31]*N for _ in range(N)]

for i in range(N-1, -1, -1):
    for j in range(i, N):
        if i == j:
            dp[i][j] = 0
            continue
        temp = 2 << 31
        for k in range(i, j):
            temp = min(temp, dp[i][k]+dp[k+1][j] +
                       diag[i][0]*diag[k][1]*diag[j][1])
        dp[i][j] = temp

print(dp[0][N-1])
