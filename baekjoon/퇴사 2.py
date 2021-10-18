"""
https://www.acmicpc.net/problem/15486
"""
n = int(input())
dp = [0]*(n+1)

for i in range(1, n+1):
    duration, profit = map(int, input().split())
    idx = i+duration - 1
    if idx <= n:
        dp[idx] = max(dp[i-1]+profit, dp[idx])
    dp[i] = max(dp[i-1], dp[i])

print(dp[n])
