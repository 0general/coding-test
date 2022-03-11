"""
https://www.acmicpc.net/problem/10942
"""
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [[-1]*n for _ in range(n)]

for i in range(n-1, -1, -1):  # index 주의
    for j in range(i, n):
        if i == j:
            dp[i][j] = 1
            continue
        if arr[i] == arr[j] and i+1 == j:
            dp[i][j] = 1
            continue
        # dp배열을 여기서 확인하기 때문에 행의 역순으로 dp를 채워야한다.
        if arr[i] == arr[j] and dp[i+1][j-1]:
            dp[i][j] = 1
            continue
        dp[i][j] = 0

for _ in range(int(input())):
    s, e = map(int, input().split())
    s -= 1
    e -= 1
    print(dp[s][e])
