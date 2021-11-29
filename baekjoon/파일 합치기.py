"""
https://www.acmicpc.net/problem/11066

참고 : https://www.acmicpc.net/board/view/31312
"""
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
    # dp[i][j] = [ 비용 , i부터 j까지 처리한 파일 크기 ]
    for i in range(n):
        dp[i][i] = [0, arr[i]]  # i부터 i까지의 합산 비용은 0, 파일 크기는 arr[i]

    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            dp[i][j][1] = dp[i][i][1] + dp[i+1][j][1]  # 파일 크기 합
            dp[i][j][0] = dp[i][i][0] + dp[i+1][j][0]  # 비용 일부 갱신
            for k in range(i+1, j):
                dp[i][j][0] = min(dp[i][j][0], dp[i][k][0]+dp[k+1][j][0])
            dp[i][j][0] += dp[i][j][1]  # 비용 최종 갱신

    print(dp[0][n-1][0])
