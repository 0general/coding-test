"""
https://www.acmicpc.net/problem/19622
"""
import sys

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# i번째 회의를 진행 or 안 진행
dp = [[0, 0] for _ in range(N)]
dp[0][0] = arr[0][2]
for i in range(1, N):
    dp[i][0] = max(dp[i-2]) + arr[i][2]
    dp[i][1] = max(dp[i-1])

print(max(dp[N-1]))
