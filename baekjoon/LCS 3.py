"""
https://www.acmicpc.net/problem/1958
"""
import sys

input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()
c = input().rstrip()

n = len(a)
m = len(b)
l = len(c)

dp = [[[0 for _ in range(l)] for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        for k in range(l):
            if a[i] == b[j] and b[j] == c[k]:
                if i >= 1 and j >= 1 and k >= 1:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                else:
                    dp[i][j][k] = 1
            if i >= 1:
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k])
            if j >= 1:
                dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k])
            if k >= 1:
                dp[i][j][k] = max(dp[i][j][k], dp[i][j][k-1])

print(dp[n-1][m-1][l-1])
