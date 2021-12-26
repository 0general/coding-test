"""
https://www.acmicpc.net/problem/18870
"""
import sys

input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
dp = [0]*n
s = []
for i in range(n):
    s.append((i, ls[i]))

s.sort(key=lambda x: (x[1], x[0]))
for i in range(1, n):
    if s[i][1] > s[i-1][1]:
        dp[s[i][0]] = dp[s[i-1][0]]+1
    else:
        dp[s[i][0]] = dp[s[i-1][0]]

print(*dp)
