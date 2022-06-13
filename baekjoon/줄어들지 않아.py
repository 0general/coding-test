"""
https://www.acmicpc.net/problem/2688
"""
import sys

input = sys.stdin.readline

dp = [[0]*10 for _ in range(65)]
dp[1] = [i for i in range(1, 11)]
for i in range(2, 65):
    dp[i][0] = dp[i-1][0]
    for j in range(1, 10):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

for _ in range(int(input())):
    n = int(input())
    print(dp[n][9])
