"""
https://www.acmicpc.net/problem/21923
"""
import sys
sys.setrecursionlimit(int(1e7))
input = sys.stdin.readline
INF = -10000000001

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
UP = 1
DOWN = 0

dp = [[[INF, INF] for _ in range(M)] for _ in range(N)]


def solve(i, j, st):
    if i < 0 or j < 0 or i >= N or j >= M:
        return INF
    if dp[i][j][st] != INF:
        return dp[i][j][st]

    if st == UP:
        dp[i][j][st] = max(solve(i+1, j, st), solve(i, j-1, st))+arr[i][j]
    else:
        dp[i][j][st] = max(solve(i-1, j, st), solve(i, j-1,
                           st), solve(i, j, UP)) + arr[i][j]
    return dp[i][j][st]


dp[N-1][0][UP] = arr[N-1][0]

print(solve(N-1, M-1, DOWN))
