"""
https://www.acmicpc.net/problem/7579
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())  # N개 앱, 필요한 바이트 양 : M
app = list(map(int, input().split()))
cost = list(map(int, input().split()))
MAX = sum(cost)
ans = MAX if M > 0 else 0

# dp[i][j] : i번째까지 j의 cost를 가지고 만들수 있는 최대의 byte
dp = [[0 for _ in range(MAX+1)] for _ in range(N)]

for i in range(N):
    for j in range(MAX+1):
        if cost[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], app[i]+dp[i-1][j-cost[i]])
        if dp[i][j] >= M:
            ans = min(ans, j)

print(ans)
