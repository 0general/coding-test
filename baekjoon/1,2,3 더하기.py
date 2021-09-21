"""
https://www.acmicpc.net/problem/9095
"""
import sys

input = sys.stdin.readline

t = int(input())

# n은 11보다 작은 양수
dp = [1] * 11
dp[1], dp[2] = 1, 2
for _ in range(t):
    n = int(input())
    for i in range(3, n+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        # 수 (i-3)에서 3 더하는 경우, (i-2)에서 2 더하는 경우, (i-1)에서 1 더하는 경우
    print(dp[n])
