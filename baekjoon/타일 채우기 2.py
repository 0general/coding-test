"""
https://www.acmicpc.net/problem/13976
"""
n = int(input())
dp = [[0, 0, 0] for _ in range(2)]

dp[0] = [0, 0, 1]  # 1칸 차는 경우, 2칸 차는 경우, 3칸 차는 경우
dp[1] = [0, 2, 0]

if n <= 1:
    print(dp[n][1])
else:
    for _ in range(2, n+1):
        temp = [0, 0, 0]
        temp[0] = dp[1][1] % 1000000007
        temp[1] = (dp[1][2]*2 + dp[1][0]) % 1000000007
        temp[2] = (dp[1][1] + dp[0][2]) % 1000000007
        dp = [dp[1], temp]
    print(dp[1][2])
