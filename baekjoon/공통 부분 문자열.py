"""
https://www.acmicpc.net/problem/5582
"""
import sys

input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

n, m = len(a), len(b)
dp = [[0]*m for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(m):
        if a[i] == b[j]:
            dp[i][j] = 1
            if i >= 1 and j >= 1:
                dp[i][j] += dp[i-1][j-1]
            ans = max(ans, dp[i][j])

print(ans)
