"""
https://www.acmicpc.net/problem/2629
"""
import sys

R = 40001
input = sys.stdin.readline

w = int(input())
weights = list(map(int, input().split()))
dp = [[False]*(R) for _ in range(w)]
dp[0][0] = True
dp[0][weights[0]] = True
n = int(input())
marbles = list(map(int, input().split()))

for i in range(1, w):
    for j in range(R):
        if dp[i-1][j]:
            dp[i][j] = True
            num = j+weights[i]
            if num < R and not dp[i][num]:
                dp[i][num] = True
            num = abs(j-weights[i])
            if not dp[i][num]:
                dp[i][num] = True


for m in marbles:
    if dp[w-1][m]:
        print('Y', end=' ')
    else:
        print('N', end=' ')
