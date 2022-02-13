"""
https://www.acmicpc.net/problem/17404
"""
import sys

input = sys.stdin.readline

n = int(input())
INF = int(1e6)+1
# 첫 번째 집이 빨, 초, 파로 시작했을 때, i번째 집 색상이 빨 초 파일 때의 비용
dp = [[INF, INF, INF] for _ in range(3)]

r, g, b = map(int, input().split())
dp[0][0] = r
dp[1][1] = g
dp[2][2] = b
for _ in range(n-1):
    r, g, b = map(int, input().split())
    for i in range(3):
        arr = [INF, INF, INF]
        if min(dp[i][1], dp[i][2]) != INF:
            arr[0] = r+min(dp[i][1], dp[i][2])
        if min(dp[i][0], dp[i][2]) != INF:
            arr[1] = g+min(dp[i][0], dp[i][2])
        if min(dp[i][0], dp[i][1]) != INF:
            arr[2] = b+min(dp[i][0], dp[i][1])
        dp[i] = arr

print(min(dp[0][1], dp[0][2], dp[1][0], dp[1][2], dp[2][0], dp[2][1]))
