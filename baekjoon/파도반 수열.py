"""
https://www.acmicpc.net/problem/9461
"""

dp = [0, 1, 1, 1, 2, 2, 3]

for i in range(7, 101):
    dp.append(dp[i-1]+dp[i-5])

for _ in range(int(input())):
    print(dp[int(input())])
