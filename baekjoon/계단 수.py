"""
https://www.acmicpc.net/problem/1562
"""

N = int(input())

dp = [[[0]*(1 << 10) for _ in range(10)] for _ in range(N)]

m = 1000000000

for i in range(1, 10):
    dp[0][i][1 << i] = 1

for n in range(1, N):
    for i in range(10):
        for state in range(1 << 10):
            if i == 0:
                dp[n][i][state | 1 << i] = (
                    dp[n][i][state | 1 << i] + dp[n-1][1][state]) % m
            elif i == 9:
                dp[n][i][state | 1 << i] = (
                    dp[n][i][state | 1 << i] + dp[n-1][8][state]) % m
            else:
                dp[n][i][state | 1 << i] = (
                    dp[n][i][state | 1 << i] + dp[n-1][i-1][state]) % m
                dp[n][i][state | 1 << i] = (
                    dp[n][i][state | 1 << i] + dp[n-1][i+1][state]) % m

k = (1 << 10)-1
ans = 0

for i in range(10):
    ans += dp[N-1][i][k]

print(ans % m)
