"""
https://www.acmicpc.net/problem/11048
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dx = [-1, 0]  # 사탕이 음수인 경우는 없으므로 대각선을 고려 X
dy = [0, -1]
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        temp = 0
        for d in range(len(dx)):
            nx, ny = i+dx[d], j+dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                temp = max(graph[nx][ny], temp)
        graph[i][j] += temp

print(graph[n-1][m-1])
