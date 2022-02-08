'''
https://www.acmicpc.net/problem/14925
'''

import sys

input = sys.stdin.readline

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

# dp[i][j] = [i][j]가 정사각형의 오른쪽 가장 아래 칸 일 때 가장 큰 정사각형의 길이
dp = [[0]*n for _ in range(m)]
ans = 0

for i in range(m):
    for j in range(n):
        if arr[i][j] > 0:
            continue
        if i > 0 and j > 0:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        else:
            dp[i][j] = 1
        ans = max(ans, dp[i][j])

print(ans)
