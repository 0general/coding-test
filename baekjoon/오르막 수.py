"""
https://www.acmicpc.net/problem/11057
"""
# 길이 n
n = int(input())
dp = [0] * (n+1)
dp[1] = [1]*10 # 오르막수의 마지막 자릿수별 개수
for i in range(1, 10): # 누적합 다음 단계에서는 어차피 현재 숫자보다 작거나 같은 모든 숫자의 개수들을 합해서 갖게 됨.
    dp[1][i] += dp[1][i-1] # dp의 마지막 열은 해당 자릿수의 모든 오르막 수의 합을 갖고 있다.

for i in range(2,n+1):
    dp[i] = [dp[i-1][j] % 10007 for j in range(10)]
    for k in range(1, 10):
        dp[i][k] += dp[i][k-1]

print(dp[n][-1] % 10007)