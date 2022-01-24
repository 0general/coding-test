"""
https://www.acmicpc.net/problem/9252
"""
import sys

input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

n = len(a)
m = len(b)

dp = [["" for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if a[i] == b[j]:
            if i >= 1 and j >= 1:
                dp[i][j] = dp[i-1][j-1] + a[i]
            else:
                dp[i][j] = a[i]
        if i >= 1 and len(dp[i-1][j]) > len(dp[i][j]):
            dp[i][j] = dp[i-1][j]
        if j >= 1 and len(dp[i][j-1]) > len(dp[i][j]):
            dp[i][j] = dp[i][j-1]

if len(dp[n-1][m-1]) == 0:
    print(0)
else:
    print(len(dp[n-1][m-1]))
    print(dp[n-1][m-1])
