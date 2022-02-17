"""
https://www.acmicpc.net/problem/14852
"""
n = int(input())

mod = 1000000007

dp = [[0, 0] for _ in range(n+1)]  # 다 차있는 경우, 한 칸만 채워진 경우

dp[0] = [1, 0]
dp[1] = [2, 2]

for i in range(2, n+1):
    dp[i][0] = (dp[i-2][0] + dp[i-1][0]*2 + dp[i-1][1]) % mod
    dp[i][1] = (dp[i-1][0]*2 + dp[i-1][1]) % mod

print(dp[n][0])
