"""
https://www.acmicpc.net/problem/1520
DFS+DP DP를 이렇게 쓰기도 한다는 걸 알아둬야 한다. 대표적인 유형으로 기억해둘 것. 
https://sihyungyou.github.io/baekjoon-1520/ 
풀이 참고
"""
import sys

sys.setrecursionlimit(25000)  # 250000으로 메모리 초과 나서 하나 줄여봄


def dfs(i, j):
    if i == m-1 and j == n-1:
        return 1
    else:
        if dp[i][j] == -1:
            dp[i][j] = 0
            for k in range(4):
                x, y = i+dx[k], j+dy[k]
                if 0 <= x < m and 0 <= y < n and arr[x][y] < arr[i][j]:
                    dp[i][j] += dfs(x, y)
    return dp[i][j]


input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1]*n for _ in range(m)]
dp[m-1][n-1] = 1

print(dfs(0, 0))
