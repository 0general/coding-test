"""
https://www.acmicpc.net/problem/7569
"""
import sys
from collections import deque


def bfs(zero_num):
    dx = [0, 0, 0, 1, 0, -1]
    dy = [0, 0, 1, 0, -1, 0]
    dz = [1, -1, 0, 0, 0, 0]
    while q:
        h, n, m, cnt = q.popleft()
        for i in range(len(dx)):
            z, x, y = h+dz[i], n+dx[i], m+dy[i]
            if 0 <= z < H and 0 <= x < N and 0 <= y < M and not visited[z][x][y] and graph[z][x][y] == 0:
                visited[z][x][y] = True
                zero_num -= 1  # 익지 않은 토마토 수 줄이기
                if zero_num == 0:
                    return cnt + 1
                q.append((z, x, y, cnt+1))
    if zero_num:
        return -1


input = sys.stdin.readline
q = deque()

M, N, H = map(int, input().split())
visited = [[[False]*M for _ in range(N)] for _ in range(H)]
graph = []
zero_num = 0

for h in range(H):
    arr = []
    for n in range(N):
        l = list(map(int, input().rstrip().split()))
        for m in range(M):
            if l[m] == 1:  # 이미 익어있는 토마토면
                visited[h][n][m] = True
                q.append((h, n, m, 0))
            elif l[m] == 0:  # 익어야 하는 토마토의 개수
                zero_num += 1
        arr.append(l)
    graph.append(arr)

if zero_num == 0:
    print(0)
else:
    print(bfs(zero_num))
