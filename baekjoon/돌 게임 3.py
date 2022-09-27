"""
https://www.acmicpc.net/problem/9657
"""
dp = ['' for _ in range(1001)]
dp[1] = 'SK'
dp[2] = 'CY'
dp[3] = 'SK'
dp[4] = 'SK'
for i in range(5, 1001):
    dp[i] = 'SK'
    if dp[i-1] == 'SK' and dp[i-3] == 'SK' and dp[i-4] == 'SK':
        dp[i] = 'CY'

print(dp[int(input())])
