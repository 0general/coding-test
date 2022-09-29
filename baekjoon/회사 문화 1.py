"""
https://www.acmicpc.net/problem/14267
"""
import sys
sys.setrecursionlimit(100010)
input = sys.stdin.readline

n, m = map(int, input().split())

cpl = [0 for _ in range(n+1)]

dp = [-1 for _ in range(n+1)]
dp[1] = 0

sup = [0] + list(map(int, input().split()))


def dfs(x):
    if dp[x] != -1:
        return dp[x]
    dp[x] = cpl[x] + dfs(sup[x])
    return dp[x]


for _ in range(m):
    i, w = map(int, input().split())
    cpl[i] += w

for i in range(1, n+1):
    print(dfs(i), end=' ')
