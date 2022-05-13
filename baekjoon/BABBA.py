"""
https://www.acmicpc.net/problem/9625
"""
import sys

k = int(sys.stdin.readline())

dp = [1, 0]  # [A,B]

for _ in range(k):
    A = dp[1]
    B = sum(dp)
    dp = [A, B]

print(*dp)
