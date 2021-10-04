"""
https://www.acmicpc.net/problem/16194
"""
n = int(input())
dp = [0] + list(map(int, input().split()))

for now in range(2, n+1):
    for i in range(1, now//2 + 1):
        dp[now] = min(dp[now], dp[i] + dp[now-i])

print(dp[n])
