"""
https://www.acmicpc.net/problem/15992
"""
import sys

input = sys.stdin.readline
MAX = 1000000009
dp = [[[0, 0, 0] for _ in range(1001)] for _ in range(1001)]
dp[1][1][0] = 1
dp[2][1][1] = 1
dp[2][2][0] = 1
dp[3][1][2] = 1
dp[3][2][0] = 1
dp[3][2][1] = 1
dp[3][3][0] = 1

for i in range(4, 1001):
    for j in range(1, 1001):
        dp[i][j][0] = sum(dp[i-1][j-1]) % MAX
        dp[i][j][1] = sum(dp[i-2][j-1]) % MAX
        dp[i][j][2] = sum(dp[i-3][j-1]) % MAX


for _ in range(int(input())):
    n, m = map(int, input().split())
    print(sum(dp[n][m]) % MAX)
