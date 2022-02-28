"""
https://www.acmicpc.net/problem/14502
"""
# 사실 deepcopy는 많은 시간을 잡아먹고 itertools는 지원하지 않는 코딩테스트도 많으므로
# 다시 deepcopy와 combinations를 사용하지 않는 방식으로 다시 풀어볼 것을 권장한다.
import sys
from collections import deque
from copy import deepcopy
from itertools import combinations as cm

input = sys.stdin.readline


def bfs(v, number):
    q = deque(virus)
    while q:
        x, y = q.popleft()
        for d in dir:
            nx, ny = x+d[0], y+d[1]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if not v[nx][ny] and arr[nx][ny] == 0:
                v[nx][ny] = True
                number -= 1
                q.append((nx, ny))
    return number


n, m = map(int, input().split())
arr = []
virus = []
walls = []
dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited = [[False]*m for _ in range(n)]
num = 0  # 빈 칸 수
ans = 0

for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(m):
        if arr[i][j] == 2:  # 바이러스면
            virus.append((i, j))
            visited[i][j] = True
        elif arr[i][j] == 1:  # 벽이면
            visited[i][j] = True
        else:  # 빈 칸이면
            num += 1
            walls.append((i, j))

for comb in list(cm(walls, 3)):
    for i, j in comb:
        arr[i][j] = 1
        visited[i][j] = True
    v = deepcopy(visited)
    ans = max(ans, bfs(v, num-3))
    if ans == num-3:
        break
    for i, j in comb:
        arr[i][j] = 0
        visited[i][j] = False

print(ans)
