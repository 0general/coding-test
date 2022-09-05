"""
https://www.acmicpc.net/problem/21610
"""
import sys

input = sys.stdin.readline

dir = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
# N 크기 격자, M 번 이동 명령
N, M = map(int, input().split())
# 물동이
bottle = [list(map(int, input().split())) for _ in range(N)]
clist = []

visited = [[False]*N for _ in range(N)]


def cloud():  # 구름 생성은 구름이 사라진 칸이 아니어야 한다.
    global visited
    for i in range(N):
        for j in range(N):
            if bottle[i][j] >= 2 and not visited[i][j]:
                clist.append((i, j))
                bottle[i][j] -= 2
    visited = [[False]*N for _ in range(N)]  # visited 갱신


def move(d, s): # 구름 이동
    global clist, visited
    for idx, cloud in enumerate(clist):
        ni, nj = cloud[0] + dir[d][0]*s, cloud[1] + dir[d][1]*s
        ni %= N
        nj %= N
        clist[idx] = (ni, nj)
    increase()


def increase(): # 물 증가
    global clist, visited
    for i, j in clist:
        bottle[i][j] += 1
        visited[i][j] = True
    copy()


def copy(): # 물 증가한 칸에 물복사
    global clist
    while clist:
        i, j = clist.pop()
        for d in [(-1, -1), (1, 1), (1, -1), (-1, 1)]:
            ni, nj = i + d[0], j + d[1]
            if ni < 0 or nj < 0 or ni >= N or nj >= N or bottle[ni][nj] == 0:
                continue
            bottle[i][j] += 1
    cloud()


def sum():
    ans = 0
    for i in range(N):
        for j in range(N):
            ans += bottle[i][j]
    return ans


clist.extend([(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)])

for _ in range(M):
    d, s = map(int, input().split())
    d -= 1
    s %= N
    move(d, s)

print(sum())
