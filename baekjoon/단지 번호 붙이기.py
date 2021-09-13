# 지도의 크기 n
from collections import deque

n = int(input())

house = [list(map(int, list(input()))) for _ in range(n)]

# 위 , 오른쪽, 아래, 왼쪽
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visit = [[False]*n for _ in range(n)]


def bfs(x, y, cnt):
    cnt += 1
    count = 0
    queue = deque()
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        if visit[x][y]:
            continue
        visit[x][y] = True
        count += 1
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if not visit[nx][ny] and house[nx][ny]:
                    queue.append([nx, ny])

    return cnt, count


cnt = 0
hcnt = []

for i in range(n):
    for j in range(n):
        if not visit[i][j] and house[i][j]:
            cnt, count = bfs(i, j, cnt)
            hcnt.append(count)

hcnt.sort()
print(cnt)
for i in range(len(hcnt)):
    print(hcnt[i])
