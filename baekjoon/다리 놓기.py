"""
https://www.acmicpc.net/problem/1010
"""
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    dp = [1]
    for i in range(1, m+1):
        dp.append(i*dp[i-1])
    print(dp[m]//(dp[m-n]*dp[n]))
