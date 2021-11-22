"""
https://www.acmicpc.net/problem/15989
"""
dp = [[0, 0, 0] for _ in range(10001)]
dp[0] = [1, 1, 1]  # 초기화
# dp[num] = [3으로 끝나는 경우, 2로 끝나는 경우(누적합 3,2), 1로 끝나는 경우(누적합 3,2,1)]
# 내림차순으로 생각했을 때 3으로 끝나는 경우는 num-3 숫자에서도 3으로 끝나야 함.
# 2로 끝나는 경우는 num-2 숫자에서 3으로 끝나도 가능
# 1로 끝나는 경우는 num-1 숫자에서 어떤 숫자로 끝나도 상관없음
for i in range(1, len(dp)):
    if i-3 >= 0:
        dp[i][0] = dp[i-3][0]
    if i-2 >= 0:
        dp[i][1] = dp[i][0] + dp[i-2][1]
    if i-1 >= 0:
        dp[i][2] = dp[i][1] + dp[i-1][2]

t = int(input())
for _ in range(t):
    print(dp[int(input())][2])
