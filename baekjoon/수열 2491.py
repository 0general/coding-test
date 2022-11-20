"""
https://www.acmicpc.net/problem/2491
"""
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [[1, 1] for _ in range(N)]  # i번째 수가 오름차순일 때, 내림차순일 때
mx = 1

for i in range(1, N):
    if arr[i-1] <= arr[i]:
        dp[i][0] = dp[i-1][0] + 1
    if arr[i] <= arr[i-1]:
        dp[i][1] = dp[i-1][1] + 1
    mx = max(dp[i][0], dp[i][1], mx)

print(mx)
