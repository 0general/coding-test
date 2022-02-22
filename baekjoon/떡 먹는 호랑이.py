"""
https://www.acmicpc.net/problem/2502
"""
import sys

input = sys.stdin.readline

d, k = map(int, input().split())

dp = [1]*(31)
for i in range(3, 31):
    dp[i] = dp[i-1]+dp[i-2]

# k = a*dp[i-2] + b*dp[i-1]
# k - a*dp[i-2] = b*dp[i-1]
# (k - a*dp[i-2])/dp[i-1] = b
for A in range(1, 100001):
    if (k-dp[d-2]*A) % dp[d-1]:
        continue
    else:
        print(A)
        print((k-dp[d-2]*A)//dp[d-1])
        break
