"""
https://www.acmicpc.net/problem/17425
"""
import sys

input = sys.stdin.readline

INF = int(1e6)
dp = [1]*(INF + 1)

for i in range(2, INF + 1):
    j = 1
    while i*j <= INF:
        dp[i*j] += i
        j += 1

for i in range(2, INF+1):
    dp[i] += dp[i-1]

for _ in range(int(input())):
    a = int(input())
    print(dp[a])
