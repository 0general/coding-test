"""
https://www.acmicpc.net/problem/1103
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(2510)

n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
INF = 2501

visited = [[False for _ in range(m)] for _ in range(n)]
dp = [[INF for _ in range(m)] for _ in range(n)]


def dfs(i, j):
    if visited[i][j]:
        return dp[i][j]
    visited[i][j] = True
    if arr[i][j] != "H":
        arr[i][j] = int(arr[i][j])
    temp = 0
    for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = i+d[0]*arr[i][j], j+d[1]*arr[i][j]
        if nx < 0 or ny < 0 or nx >= n or ny >= m or arr[nx][ny] == "H":
            continue
        temp = max(temp, dfs(nx, ny))
        if temp >= INF:
            return INF
    dp[i][j] = temp + 1
    return dp[i][j]


print(dp[0][0] if dfs(0, 0) < INF else -1)
