"""
https://www.acmicpc.net/problem/9465
"""
import sys

input = sys.stdin.readline

# test case
t = int(input())

for _ in range(t):
    # number of column
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]
    for i in range(1, n):
        if i == 1:  # 두번째 열까지의 스티커 최대 점수 갱신
            dp[0][i] += dp[1][i-1]  # 0행 1열 스티커를 뜯기로 했을 때, 1행 0열을 반드시 뜯어야 이득
            dp[1][i] += dp[0][i-1]  # 1행 1열 스티커를 뜯기로 했을 때, 0행 1열을 반드시 뜯어야 이득
        else:  # 세번째 이상의 열에 해당하는 스티커를 뜯을 때의 최대 점수 갱신
            # 두 가지 경우를 고려해서 갱신해야한다.
            # i-1열의 같은 행 스티커는 뜯을 수 없으므로 무시
            # 첫번째는 i-1열의 다른 행을 뜯을 경우이다.
            # 두번째는 i-2열의 다른 행을 뜯을 경우이다. 이 때는 i-1열의 어떤 스티커도 뜯을 수 없다
            dp[0][i] += max(dp[1][i-1], dp[1][i-2])
            dp[1][i] += max(dp[0][i-1], dp[0][i-2])
    print(max(dp[0][n-1], dp[1][n-1]))
