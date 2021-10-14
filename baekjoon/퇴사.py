"""
https://www.acmicpc.net/problem/14501
"""
n = int(input())
dp = [0]*(n+1)

for i in range(1, n+1): # i번째 날
    duration, profit = map(int, input().split()) # i번째 날에 받은 상담
    idx = i+duration - 1 #상담 종료 날짜
    if idx <= n: # 퇴사 전까지 상담 종료라면
        dp[idx] = max(dp[i-1]+profit, dp[idx]) # 상담 종료 날짜에 가질 최대 이익
    dp[i] = max(dp[i-1], dp[i]) # i번째 날까지 벌 수 있는 최대 이익은 전날의 이익과 오늘의 이익 중 높은 것 선택

print(dp[n])