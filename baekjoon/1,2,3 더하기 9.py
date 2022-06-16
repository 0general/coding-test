"""
https://www.acmicpc.net/problem/16195
"""
import sys
input = sys.stdin.readline

dp = [[0]*1001 for _ in range(1001)]
ans = [[0]*1001 for _ in range(1001)]
MAX = 1000000009

dp[0][0] = 1
for i in range(1, 1001):
    for k in range(1, 1001):
        for j in [1, 2, 3]:
            if i-j >= 0:
                dp[i][k] += dp[i-j][k-1]
                dp[i][j] %= MAX
        ans[i][k] = (ans[i][k-1] + dp[i][k]) % MAX

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(ans[n][m])
