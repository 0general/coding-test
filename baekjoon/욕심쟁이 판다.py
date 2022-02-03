"""
https://www.acmicpc.net/problem/1937
"""
import sys

input = sys.stdin.readline
sys.setrecursionlimit(250010)


def dfs(x, y):
    # 이전의 위치보다 더 많은 대나무가 있는 곳으로 가야한다.
    # 그 경로의 길이를 dp로 저장해두고 반환해야 함.
    if dp[x][y] != 0:
        return dp[x][y]
    temp = 0
    for i in range(4):
        nx, ny = x+d[i][0], y+d[i][1]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if arr[nx][ny] > arr[x][y]:
            temp = max(temp, dfs(nx, ny))
    dp[x][y] = temp + 1
    return dp[x][y]


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dp = [[0]*n for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))
        if ans == n*n:
            break
    else:
        continue
    break

print(ans)
