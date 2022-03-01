"""
https://www.acmicpc.net/problem/1311
"""
import sys

input = sys.stdin.readline
MAX = 200001

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[MAX]*(1 << n) for _ in range(n)]

for i in range(n):  # i 사람이 할 일
    for k in range(n):  # k번째 일
        if i == 0:
            dp[i][1 << k] = arr[i][k]
            continue
        for j in range(1 << n):
            if dp[i-1][j] == MAX:
                continue
            if (j & 1 << k) == 0:  # 겹치지 않으면
                dp[i][j | 1 << k] = min(
                    dp[i][j | 1 << k], dp[i-1][j]+arr[i][k])


print(min(dp[n-1]))
