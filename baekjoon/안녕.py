"""
https://www.acmicpc.net/problem/1535
"""
import sys

input = sys.stdin.readline

n = int(input())
st = list(map(int, input().split()))
dl = list(map(int, input().split()))
dp = [[0 for _ in range(100)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, 100):
        if j >= st[i-1]:
            dp[i][j] = dp[i-1][j-st[i-1]]+dl[i-1]
        dp[i][j] = max(dp[i][j-1], dp[i-1][j], dp[i][j])

print(dp[n][99])
