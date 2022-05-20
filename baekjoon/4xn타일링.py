"""
https://www.acmicpc.net/problem/11333
"""
import sys

input = sys.stdin.readline

dp = [[0, 0, 0] for _ in range(10001)]  # 다 채워지는 경우, 1개만 차는 경우, 3개만 차는 경우
dp[0][0] = 1
dp[1][2] = 2
dp[3][0] = 3
dp[3][1] = 2


for i in range(4, len(dp)):
    # i-2에서 세 칸만 채워져있을 때 (1x3 하나+3x1 2개), i-3에서 완벽할 때 (1x3 4개), i-3에서 한 칸만 채워져있을 때 (1x3 4개+3x1 하나)
    dp[i][0] = (dp[i-2][2] + dp[i-3][0] + dp[i-3][1]) % 1000000007
    # i-2에서 세 칸만 채워져있을 때 (1x3 하나+3x1 하나), i-3에서 한 칸만 채워져있을 때 (1x3 4개)
    dp[i][1] = (dp[i-2][2] + dp[i-3][1]) % 1000000007
    # i-1에서 완벽할 때 (3x1 하나) 위 아래로 총 두 번, i-3에서 세 칸만 채워져있을 때 (1x3 4개)
    dp[i][2] = (dp[i-1][0]*2 + dp[i-3][2]) % 1000000007

for _ in range(int(input())):
    n = int(input())
    print(dp[n][0])
