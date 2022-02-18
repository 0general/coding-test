"""
https://www.acmicpc.net/problem/2146
"""
import sys
from collections import deque

input = sys.stdin.readline


def check_land():
    while q:
        x, y = q.popleft()
        arr[x][y] = num
        for dd in d:
            nx, ny = x+dd[0], y + dd[1]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if not visited[nx][ny][0] and arr[nx][ny] == 1:
                visited[nx][ny][0] = True
                q.append((nx, ny))
            elif not visited[nx][ny][0] and arr[nx][ny] == 0:
                visited[nx][ny] = [1, num]
                bridge.append((nx, ny))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[[False, 0] for _ in range(N)] for _ in range(N)]
q = deque()
ans = 10001
bridge = deque()
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

num = 1
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and not visited[i][j][0]:
            visited[i][j][0] = True
            q.append((i, j))
            check_land()
            num += 1

while bridge:
    x, y = bridge.popleft()
    for dd in d:
        nx, ny = x+dd[0], y+dd[1]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        if not visited[nx][ny][0] and arr[nx][ny] == 0:  # 아직 도달한 적 없는 바다 위
            visited[nx][ny] = [visited[x][y][0]+1, visited[x][y][1]]
            bridge.append((nx, ny))
        elif arr[nx][ny] != 0 and arr[nx][ny] != visited[x][y][1]:  # 다른 땅에 바로 닿을 때
            ans = min(ans, visited[x][y][0])
        elif arr[nx][ny] == 0 and visited[nx][ny][1] != visited[x][y][1]:  # 다른 땅에서의 최단 거리와 만났을 때
            ans = min(ans, visited[nx][ny][0]+visited[x][y][0])


print(ans)
