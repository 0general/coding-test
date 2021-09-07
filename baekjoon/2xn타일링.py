'''
가장 기본적인 dP문제
https://www.acmicpc.net/problem/11726
'''

n = int(input())

dp = [1]*(n+1)
if n >= 2:
    for i in range(2, n+1):
        dp[i] = dp[i-1]+dp[i-2]
print(dp[n] % 10007)
