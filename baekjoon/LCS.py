"""
https://www.acmicpc.net/problem/9251
"""
import sys

input = sys.stdin.readline
x = input().rstrip()
y = input().rstrip()

xl = len(x)
yl = len(y)

dp = [[0]*yl for _ in range(xl)]

for i in range(xl):
    for j in range(yl):
        if i == 0 and j == 0:
            dp[i][j] += (x[i] == y[j])
        elif i == 0:
            dp[i][j] = max(dp[i][j-1], int(x[i] == y[j]))
        elif j == 0:
            dp[i][j] = max(dp[i-1][j], int(x[i] == y[j]))
        else:
            if x[i] == y[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[xl-1][yl-1])
