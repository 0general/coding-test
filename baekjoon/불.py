"""
https://www.acmicpc.net/problem/5427
"""
import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

T = int(input())
for _ in range(T):
    W, H = map(int, input().split())
    graph = []
    q = deque()
    flag = False
    visited = [[False]*W for _ in range(H)]
    fvisited = [[False]*W for _ in range(H)]
    fire = deque()
    for i in range(H):
        graph.append(list(input().rstrip()))
        for j in range(W):
            if graph[i][j] == "*":
                fire.append((i, j))
            elif graph[i][j] == "@":
                visited[i][j] = True
                graph[i][j] == "."  # 시작 위치 찾아놨으니
                q.append((i, j))  # 시작 위치는 하나
    cnt = 1
    while q:
        for _ in range(len(fire)):  # 불 먼저 옮겨 붙고
            fx, fy = fire.popleft()
            for k in range(len(dx)):
                nx, ny = fx+dx[k], fy+dy[k]
                if 0 <= nx < H and 0 <= ny < W and graph[nx][ny] == ".":
                    graph[nx][ny] = "*"
                    fire.append((nx, ny))
        for _ in range(len(q)):
            x, y = q.popleft()
            for k in range(len(dx)):
                nx, ny = x+dx[k], y+dy[k]
                if 0 <= nx < H and 0 <= ny < W:
                    if graph[nx][ny] == "." and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                else:
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
        cnt += 1
    if flag:
        print(cnt)
    else:
        print("IMPOSSIBLE")
