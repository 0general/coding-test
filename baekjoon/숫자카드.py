"""
https://www.acmicpc.net/problem/2591
"""
import sys

arr = list(sys.stdin.readline().rstrip())
n = len(arr)
dp = [1]*n

for i in range(1, n):
    if arr[i] == '0':
        dp[i] = dp[i-2]
        continue
    dp[i] = dp[i-1]
    if arr[i-1] != '0' and int(arr[i-1]+arr[i]) <= 34:
        dp[i] += dp[i-2]

print(dp[n-1])
