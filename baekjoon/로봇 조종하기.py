'''
DP
https://www.acmicpc.net/problem/2169
'''
n, m = map(int, input().split())

value = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
dp[0][0] = value[0][0]

for i in range(n):
    if i == 0:
        for j in range(1, m):
            dp[i][j] = value[i][j] + dp[i][j-1]
    elif i == n-1:
        dp[i][0] = dp[i-1][0] + value[i][0]
        for j in range(1, m):
            dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + value[i][j]
    else:
        for j in range(m):  # 왼쪽에서 오른쪽
            if j == 0:
                dp[i][j] = dp[i-1][j] + value[i][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + value[i][j]
        mx = [0]*m  # 오른쪽에서 왼쪽 값 저장할 리스트
        for k in range(-1, -m-1, -1):  # 오른쪽에서 왼쪽
            if k == -1:
                mx[k] = dp[i-1][k] + value[i][k]
            else:
                mx[k] = max(dp[i-1][k], mx[k+1]) + value[i][k]
            dp[i][k] = max(mx[k], dp[i][k])


print(dp[n-1][m-1])
