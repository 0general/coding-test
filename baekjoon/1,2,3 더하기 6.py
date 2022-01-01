"""
https://www.acmicpc.net/problem/15991
"""
dp = [[0, 0] for _ in range(100001)]  # 대칭으로 만들 수 있는 방법, 그냥 1,2,3으로 만들 수 있는 방법
dp[1] = [1, 1]
dp[2] = [2, 2]
dp[3] = [2, 4]
for i in range(4, 100001):
    if i % 2 == 0:
        dp[i][0] = (dp[i//2][1] + dp[(i-2)//2][1]) % 1000000009
    else:
        dp[i][0] = (dp[(i-1)//2][1] + dp[(i-3)//2][1]) % 1000000009
    dp[i][1] = (dp[i-1][1] + dp[i-2][1] + dp[i-3][1]) % 1000000009

for _ in range(int(input())):
    print(dp[int(input())][0])
