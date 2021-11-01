"""
https://www.acmicpc.net/problem/13398
"""
import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [[num, 0] for num in nums]
mx = dp[0][0]

for i in range(1, n):
    dp[i][0] = max(dp[i-1][0]+nums[i], nums[i])  # 자기자신을 무조건 선택하는 경우 중 가장 큰 경우
    # 자기자신을 포함하여 무조건 한 개의 수가 빠지는 경우 (나를 선택하고 앞에서 하나 빠짐, 나를 빼는 경우)
    dp[i][1] = max(dp[i-1][1]+nums[i], dp[i-1][0])
    mx = max(mx, dp[i][0], dp[i][1])

print(mx)
