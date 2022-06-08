"""
https://www.acmicpc.net/problem/13301
"""
import sys

input = sys.stdin.readline

dp = [1 for _ in range(81)]
for i in range(2, 81):
    dp[i] = dp[i-1]+dp[i-2]

n = int(input()) - 1
if n == 0:
    print(4)
else:
    print(dp[n]*4+dp[n-1]*2)
