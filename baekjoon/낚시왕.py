"""
https://www.acmicpc.net/problem/17143
"""
import sys

input = sys.stdin.readline

r, c, m = map(int, input().split())
sea = [[0 for _ in range(c)] for _ in range(r)]


for _ in range(m):
    x, y, s, d, z = map(int, input().split())  # 속력, 방향, 크기
    x -= 1
    y -= 1
    d -= 1
    sea[x][y] = (z, s, d)


def up(dist, dir, x, y):  # 이동할 거리, 방향, 현 위치
    global r
    mod = r-1
    if dist <= x:
        return x-dist, y, dir
    else:
        dist -= x
        nd = dist//mod
        k = dist % mod
        if k == 0:
            nd -= 1
            k = mod
        if nd % 2 == 0:  # 방향 바뀜
            return k, y, dir ^ 1
        else:  # 방향 안 바뀜
            return mod-k, y, dir


def down(dist, dir, x, y):
    global r
    mod = r-1
    if dist <= mod-x:
        return x+dist, y, dir
    else:
        dist -= mod-x
        nd = dist//mod
        k = dist % mod
        if k == 0:
            nd -= 1
            k = mod
        if nd % 2 == 0:  # 방향 바뀜
            return mod-k, y, dir ^ 1
        else:  # 방향 안 바뀜
            return k, y, dir


def left(dist, dir, x, y):
    global c
    mod = c-1
    if dist <= y:
        return x, y-dist, dir
    else:
        dist -= y
        nd = dist//mod
        k = dist % mod
        if k == 0:
            nd -= 1
            k = mod
        if nd % 2 == 0:  # 방향 바뀜
            return x, k, dir ^ 1
        else:  # 방향 안 바뀜
            return x, mod-k, dir


def right(dist, dir, x, y):
    global c
    mod = c-1
    if dist <= mod-y:
        return x, y+dist, dir
    else:
        dist -= mod-y
        nd = dist//mod
        k = dist % mod
        if k == 0:
            nd -= 1
            k = mod
        if nd % 2 == 0:  # 방향 바뀜
            return x, mod-k, dir ^ 1
        else:  # 방향 안 바뀜
            return x, k, dir


def shark_move():
    global r, c, sea, shark, m
    # 모든 상어가 이동한다.
    # 새로 이동한 것이 sea에 갱신됨.
    # 이동을 마친 후에야 상어끼리 잡아먹음
    new_sea = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if sea[i][j] == 0:
                continue
            size, dist, d = sea[i][j]
            x, y = 0, 0
            if d == 0:
                x, y, d = up(dist, d, i, j)
            elif d == 1:
                x, y, d = down(dist, d, i, j)
            elif d == 2:
                x, y, d = right(dist, d, i, j)
            else:
                x, y, d = left(dist, d, i, j)
            if new_sea[x][y] == 0:
                new_sea[x][y] = (size, dist, d)
            else:
                m -= 1
                if new_sea[x][y][0] < size:
                    new_sea[x][y] = (size, dist, d)
    sea = new_sea


# 낚시 왕이 잡은 상어의 크기
answer = 0
# 낚시 횟수는 c
for j in range(c):
    # 낚시 위치 j열에 있는 상어 중에서 가장 가까운 상어를 잡는다.
    for i in range(r):
        if m == 0:
            break
        if sea[i][j] != 0:
            # 상어 사이즈를 answer에 합함
            answer += sea[i][j][0]
            # 격자 비움
            sea[i][j] = 0
            m -= 1
            break
    if m == 0:
        break
    # 상어이동
    shark_move()

print(answer)
