"""
https://www.acmicpc.net/problem/17074
"""
import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# dp[i][0] = i번째 수 안 버리고 버린 경험 없음
# dp[i][1] = i번째 수 안 버리고 버린 경험 있음
# dp[i][2] = i번째 수 버림
dp = [[0, 0, 0] for _ in range(N)] # i번째까지 정렬된 경우만 담는다
dp[0] = [1, 0, 1]
if arr[1] >= arr[0]:
    dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1  # dp[0][0]

for i in range(2, N):
    dp[i][2] = dp[i-1][0]
    if arr[i] >= arr[i-1]:
        dp[i][0] = dp[i-1][0]
        dp[i][1] += dp[i-1][1]
    if arr[i] >= arr[i-2]:
        dp[i][1] += dp[i-1][2]

print(dp[N-1][1] + dp[N-1][2])
