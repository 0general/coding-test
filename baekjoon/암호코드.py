"""
https://www.acmicpc.net/problem/2011
"""

arr = input()
n = len(arr)
dp = [0]*(n+1)
dp[0] = 1

for i in range(1, n+1):
    if i > 1 and 1 <= int(arr[i-2]) <= 2 and int(arr[i-2:i]) <= 26:
        dp[i] += dp[i-2]
    if int(arr[i-1]) != 0:
        dp[i] = (dp[i]+dp[i-1]) % 1000000
    if dp[i] == 0:
        break

print(dp[n])
