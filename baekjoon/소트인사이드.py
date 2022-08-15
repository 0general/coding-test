"""
https://www.acmicpc.net/problem/1427
"""
import sys
input = sys.stdin.readline

N = input().rstrip()

dp = [0]*10

for i in N:
    dp[int(i)] += 1

ans = ''
for i in range(9, -1, -1):
    ans += str(i)*dp[i]

print(ans)
