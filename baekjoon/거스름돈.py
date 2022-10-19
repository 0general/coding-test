"""
https://www.acmicpc.net/problem/14916
"""
import sys
input = sys.stdin.readline

n = int(input())
dp = [i//5 if i % 5 == 0 else -1 for i in range(n+1)]
for i in range(2, n+1):
    if dp[i] != -1:
        continue
    if dp[i-2] != -1:
        dp[i] = dp[i-2] + 1

print(dp[n])
