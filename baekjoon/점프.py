"""
https://www.acmicpc.net/problem/1890
"""
import sys


def check_route(i, j):
    if dp[i][j] != 0:
        return dp[i][j]
    if arr[i][j] == 0:  # 이 종료 조건 빼먹으면 무한반복을 하면서 recursion error를 일으킨다.
        return 0
    for k in [(0, 1), (1, 0)]:
        x, y = i+(k[0]*arr[i][j]), j+(k[1]*arr[i][j])
        if 0 <= x < n and 0 <= y < n:
            dp[i][j] += check_route(x, y)
    return dp[i][j]


input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[n-1][n-1] = 1

print(check_route(0, 0))
