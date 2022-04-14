"""
https://www.acmicpc.net/problem/19238
"""
import sys
from collections import deque

input = sys.stdin.readline

dir = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # 이 순서 맞춘다고 택시 승객 원칙대로 태워지지 않는다.
# 동일한 거리일 때 이 순서 상으로는 왼쪽으로 3번 이동한 승객을 먼저 만나지만 사실 태워야 하는 건 오른쪽으로 두 칸 위로 한 칸 떨어진 승객이기 때문

N, M, fuel = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]


def find_client(si, sj):
    global fuel
    if Map[si][sj] != 0 and Map[si][sj] != 1:  # 탐색 시작지가 출발지일 때
        ei, ej = Map[si][sj]
        Map[si][sj] = 0
        return taxi(si, sj, ei, ej)

    visited = [[False]*N for _ in range(N)]
    q = deque()
    visited[si][sj] = True
    q.append((si, sj, 0))

    clist = []
    while q:
        x, y, used_f = q.popleft()
        for d in dir:
            nx, ny = x + d[0], y + d[1]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if Map[nx][ny] == 0 and not visited[nx][ny] and fuel > used_f:
                visited[nx][ny] = True
                q.append((nx, ny, used_f+1))
            if Map[nx][ny] != 1 and Map[nx][ny] != 0 and fuel > used_f:
                if len(clist) == 0:
                    clist.append((used_f+1, nx, ny))
                else:
                    if clist[0][0] <= used_f+1:
                        clist.append((used_f+1, nx, ny))
                    else:
                        break
        else:
            continue
        break
    if len(clist) == 0:
        return -1
    clist.sort(key=lambda x: (x[0], x[1], x[2]))
    fuel -= clist[0][0]
    x, y = clist[0][1], clist[0][2]
    ei, ej = Map[x][y]
    Map[x][y] = 0
    return taxi(x, y, ei, ej)


def taxi(si, sj, ei, ej):
    global fuel
    # 츨발지, 목적지, 현재 가진 연료
    visited = [[False]*N for _ in range(N)]
    q = deque()
    visited[si][sj] = True
    q.append((si, sj, 0))

    while q:
        x, y, used_f = q.popleft()
        for d in dir:
            nx, ny = x + d[0], y + d[1]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if Map[nx][ny] != 1 and not visited[nx][ny] and fuel > used_f:
                if nx == ei and ny == ej:
                    fuel += used_f+1  # 주유
                    return nx, ny
                visited[nx][ny] = True
                q.append((nx, ny, used_f+1))
    return -1


x, y = map(int, input().split())
x -= 1
y -= 1
for _ in range(M):
    sx, sy, ex, ey = map(int, input().split())
    sx -= 1
    sy -= 1
    ex -= 1
    ey -= 1
    Map[sx][sy] = [ex, ey]

for _ in range(M):
    next = find_client(x, y)
    if next == -1:
        fuel = -1
        break
    x, y = next[0], next[1]

print(fuel)
