"""
https://www.acmicpc.net/problem/9660
"""
n = int(input())
# 7번째면 DY인데, mod 시  0 나오니까 dp[0] = CY
dp = ["CY", "SK", "CY", "SK", "SK", "SK", "SK", "CY"]

print(dp[n % 7])  # 앞선 결과에 따라 결정되는 승부가 7개씩 주기적으로 반복된다.
