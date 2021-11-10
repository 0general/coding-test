"""
https://www.acmicpc.net/problem/11055
"""
import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
dp = [num for num in nums]
mx = dp[0]

for i in range(1, n):
    for j in range(i-1, -1, -1):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + nums[i])
            if dp[j] == mx:
                mx = dp[i]
                break
    if dp[i] > mx:
        mx = dp[i]

print(mx)
