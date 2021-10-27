"""
https://www.acmicpc.net/problem/1912
"""
import sys
input = sys.stdin.readline

n = int(input())
dp = list(map(int, input().split()))

# 해당 숫자를 선택했을 때 최대값
answer = dp[0]
for i in range(1, n):
    dp[i] = max(dp[i-1]+dp[i], dp[i])
    if dp[i] > answer:
        answer = dp[i]

print(answer)
