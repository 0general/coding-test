"""
https://www.acmicpc.net/problem/1303
"""
import sys
input = sys.stdin.readline
ans = [0, 0]  # W, B
N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(M)]
visited = [[False for _ in range(N)] for _ in range(M)]

for i in range(M):
    for j in range(N):
        if visited[i][j]:
            continue
        visited[i][j] = True
        temp = 0
        num = 0
        if arr[i][j] == 'B':
            temp = 1
        s = []
        s.append((i, j))
        while s:
            x, y = s.pop()
            num += 1
            for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + d[0], y + d[1]
                if nx < 0 or ny < 0 or nx >= M or ny >= N or visited[nx][ny] or arr[nx][ny] != arr[x][y]:
                    continue
                visited[nx][ny] = True
                s.append((nx, ny))
        ans[temp] += num**2

print(*ans)
