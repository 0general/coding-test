"""
https://www.acmicpc.net/problem/4963
"""
import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(len(dx)):
            nowx, nowy = x+dx[i], y+dy[i]
            if 0 <= nowx < h and 0 <= nowy < w:
                if not visit[nowx][nowy]:
                    visit[nowx][nowy] = True
                    if arr[nowx][nowy] == 1:
                        queue.append((nowx, nowy))


dx = [0, 0, -1, 1, 1, -1, -1, 1]
dy = [-1, 1, 0, 0, 1, -1, 1, -1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = []
    for _ in range(h):
        arr.append(list(map(int, input().split())))
    visit = [[False] * w for _ in range(h)]
    queue = deque()
    cnt = 0
    for i in range(h):
        for j in range(w):
            if not visit[i][j]:
                visit[i][j] = True
                if arr[i][j] == 1:
                    queue.append((i, j))
                    bfs()
                    cnt += 1
    print(cnt)
