"""
https://www.acmicpc.net/problem/15993
"""
import sys

input = sys.stdin.readline

MAX = 1000000009
N = 100000
dp = [[[0, 0, 0], [0, 0, 0]] for _ in range(N+1)]  # 1,2,3으로 끝나는 경우 개수 홀,짝
dp[1] = [[1, 0, 0], [0, 0, 0]]
dp[2] = [[0, 1, 0], [1, 0, 0]]
dp[3] = [[1, 0, 1], [1, 1, 0]]
for i in range(4, len(dp)):
    dp[i][0][0] = sum(dp[i-1][1]) % MAX
    dp[i][0][1] = sum(dp[i-2][1]) % MAX
    dp[i][0][2] = sum(dp[i-3][1]) % MAX
    dp[i][1][0] = sum(dp[i-1][0]) % MAX
    dp[i][1][1] = sum(dp[i-2][0]) % MAX
    dp[i][1][2] = sum(dp[i-3][0]) % MAX


for _ in range(int(input())):
    n = int(input())
    print(sum(dp[n][0]) % MAX, sum(dp[n][1]) % MAX)
