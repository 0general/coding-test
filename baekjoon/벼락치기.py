"""
https://www.acmicpc.net/problem/14728
"""
import sys

input = sys.stdin.readline

N, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# i번째 단원까지 고려했을 때 T의 시간을 두고 가질 수 있는 최대 점수
dp = [[0 for _ in range(T+1)] for _ in range(N)]

for i in range(N):
    for j in range(1, T+1):
        if arr[i][0] > j:
            dp[i][j] = dp[i-1][j]
        else:
            if j > arr[i][0]:
                dp[i][j] = dp[i-1][j-arr[i][0]]+arr[i][1]
            dp[i][j] = max(dp[i-1][j], arr[i][1], dp[i][j])

print(dp[N-1][T])
