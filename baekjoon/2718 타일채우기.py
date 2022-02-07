"""
https://www.acmicpc.net/problem/2718
"""
import sys

input = sys.stdin.readline

# dp = [[0, 0] for _ in range(2147483648)]
dp = [[0, 0] for _ in range(12)]
dp[0] = [1, 0]  # 채워진 경우, 두 칸 비워진 경우
dp[1] = [1, 3]

# for i in range(2, 2147483648):
for i in range(2, 12):
    dp[i][0] = dp[i-1][0] + dp[i-1][1] + dp[i-2][0]
    dp[i][1] = dp[i-1][0]*3 + dp[i-1][1]

for _ in range(int(input())):
    n = int(input())
    print(dp[n])
