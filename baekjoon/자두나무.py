"""
https://www.acmicpc.net/problem/2240
"""
import sys

input = sys.stdin.readline

T, W = map(int, input().split())

dp = [[[0]*(W+1), [0]*(W+1)] for _ in range(T)]

t = {0: 1, 1: 0}
a = int(input())-1
if a == 0:
    dp[0][0][0] = 1
else:
    dp[0][1][1] = 1

for i in range(1, T):
    a = int(input()) - 1
    dp[i][t[a]] = [x for x in dp[i-1][t[a]]]
    if a == 0:
        dp[i][a][0] = dp[i-1][a][0] + 1
    for j in range(1, W+1):
        if dp[i-1][a][j] == 0 and dp[i-1][t[a]][j-1] == 0:
            continue
        dp[i][a][j] = max(dp[i-1][a][j], dp[i-1][t[a]][j-1])+1

print(max(max(dp[T-1][0]), max(dp[T-1][1])))
