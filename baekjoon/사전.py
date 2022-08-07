"""
https://www.acmicpc.net/problem/1256
"""
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
dp = [[1]*(m+1) for _ in range(n+1)]  # dp[i][j] = i개의 a와 j개의 z로 만들 수 있는 단어의 개수
# a만 있는 경우나 z만 있는 경우는 1개뿐이다.
for i in range(1, n+1):
    for j in range(1, m+1):
        # (n+m)C(n) = (n+m-1)C(n-1) + (n+m-1)C(n)
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

if dp[n][m] < k:
    print(-1)
else:
    result = ""
    while True:
        if n == 0 or m == 0:  # 남은 경우의 수는 1가지
            result += "a"*n
            result += "z"*m
            break

        temp = dp[n-1][m]  # a로 시작하는 경우
        if temp >= k:
            result += "a"
            n -= 1
        else:  # z로 시작해야 함
            result += "z"
            m -= 1
            k -= temp  # a로 시작한 문자열의 개수를 빼줌
    print(result)
