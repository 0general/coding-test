"""
https://www.acmicpc.net/problem/21611
호석님 방송 듣고 함
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

num = [[0 for _ in range(N)] for _ in range(N)]
L = N*N-1
snail = [0]*(L)
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

cnt = [0]*4


def stretch_snail():
    visited = [[False for _ in range(N)] for _ in range(N)]
    x = N**2 - 2
    i, j = 0, 0
    d = 0
    while i != N//2 or j != N//2:
        visited[i][j] = True
        num[i][j] = x
        snail[x] = arr[i][j]
        ni, nj = i + dir[d][0], j + dir[d][1]
        if ni < 0 or nj < 0 or ni >= N or nj >= N or visited[ni][nj]:
            d = (d + 1) % 4
            ni, nj = i + dir[d][0], j + dir[d][1]
        i, j = ni, nj
        x -= 1


def blizzard(di, si):
    i, j = N//2, N//2
    while si > 0:
        ni, nj = i + dir[di][0], j + dir[di][1]
        if ni < 0 or nj < 0 or ni >= N or nj >= N:
            break
        snail[num[ni][nj]] = 0
        i, j = ni, nj
        si -= 1
    compress()


def compress():
    last = 0
    for i in range(L):
        if snail[i] == 0:
            continue
        snail[last] = snail[i]
        last += 1
    for i in range(last, L):
        snail[i] = 0


def bomb():
    ok = False
    i = 0
    while i < L and snail[i] != 0:
        j = i
        while j + 1 < L and snail[j + 1] == snail[i]:
            j += 1
        if j - i + 1 >= 4:
            ok = True
            cnt[snail[i]] += j - i + 1
            for k in range(i, j+1):
                snail[k] = 0
        i = j + 1
    compress()
    return ok


def convert():
    global snail
    temp = [0]*L

    last = 0
    i = 0
    while i < L and snail[i] != 0 and last < L:
        j = i
        while j + 1 < L and snail[i] == snail[j+1]:
            j += 1
        A = j - i + 1
        B = snail[i]
        temp[last] = A
        last += 1
        if last >= L:
            break
        temp[last] = B
        last += 1

        i = j + 1

    snail = temp


stretch_snail()

dir = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
for _ in range(M):
    di, si = map(int, input().split())
    blizzard(di, si)
    flag = True
    while flag:
        flag = bomb()
    convert()

ans = 0
for i in range(1, 4):
    ans += cnt[i]*i

print(ans)
