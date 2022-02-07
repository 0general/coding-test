"""
https://www.acmicpc.net/problem/2718
"""
import sys

input = sys.stdin.readline
# 적절한 dp 크기도 찾아야 한다.
# 경우의 수가 2147483647보다 작게 주어진다고 했으므로 n 값은 22 이하로만 주어짐.
dp = [[0, 0, 0, 0] for _ in range(23)]
# 다 채워진 경우, 위 아래 두 칸이 채워지는 경우, 가운데 두 칸이 채워지는 경우, 맨 위와 맨 아래만 채워지는 경우
dp[0] = [1, 0, 0, 0]
dp[1] = [1, 2, 1, 0]

for i in range(2, 23):
    dp[i][0] = dp[i-1][0] + dp[i-2][0] + dp[i-1][1] + dp[i-1][2]
    dp[i][1] = dp[i-1][0]*2 + dp[i-1][1]
    dp[i][2] = dp[i-1][0] + dp[i-1][3]
    dp[i][3] = dp[i-1][2]

for _ in range(int(input())):
    n = int(input())
    print(dp[n][0])
