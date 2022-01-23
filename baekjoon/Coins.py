"""
https://www.acmicpc.net/problem/3067
"""
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())  # 동전의 가지 수
    dp = [0]*10001
    dp[0] = 1
    arr = list(map(int, input().split()))
    ans = int(input())
    for i in arr:
        for j in range(i, ans+1):
            if dp[j-i]:
                dp[j] += dp[j-i]
    print(dp[ans])
