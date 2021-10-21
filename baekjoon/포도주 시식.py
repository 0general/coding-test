"""
https://www.acmicpc.net/problem/2156
"""
import sys

input = sys.stdin.readline

n = int(input())
# 마지막 와인을 마시지 않을 경우도 있으로 2579 계단 오르기처럼 dp를 정의해서는 안된다.
# i번째 와인까지 결정했을 때 가질 수 있는 최대 값
# 각 와인이 가질 수 있는 선택은 3가지이다.
# [첫 번째로 마시는가, 두 번째로 마시는가, 마시지 않는가]

dp = [0]*(n)

for i in range(n):
    a = int(input())
    if i == 0:
        dp[i] = [a, 0, 0]
    else:
        dp[i] = [dp[i-1][2]+a, dp[i-1][0]+a, max(dp[i-1])]
        # 첫번째로 마시려면 앞 와인 선택 X
        # 두번째로 마시려면 앞 와인 첫번째로 마셔야
        # 안 마실거라면 앞 와인에서 결정한 최대값

print(max(dp[n-1]))
