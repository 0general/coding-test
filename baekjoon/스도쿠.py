"""
https://www.acmicpc.net/problem/2580
"""
import sys

input = sys.stdin.readline

ok = False
arr = [list(map(int, input().split())) for _ in range(9)]

pos_i = [[False for _ in range(10)] for _ in range(9)]
pos_j = [[False for _ in range(10)] for _ in range(9)]
pos_c = [[[False for _ in range(10)] for _ in range(3)] for _ in range(3)]

position = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            position.append((i, j))
            continue
        pos_i[i][arr[i][j]] = True
        pos_j[j][arr[i][j]] = True
        x, y = i//3, j//3
        pos_c[x][y][arr[i][j]] = True


def check(idx):
    global ok
    if idx >= len(position):
        ok = True
        for i in range(9):
            print(*arr[i])
        return
    i, j = position[idx]
    x, y = i//3, j//3
    for num in range(1, 10):
        if not pos_i[i][num] and not pos_j[j][num] and not pos_c[x][y][num]:
            pos_i[i][num] = True
            pos_j[j][num] = True
            pos_c[x][y][num] = True
            arr[i][j] = num
            check(idx+1)
            pos_i[i][num] = False
            pos_j[j][num] = False
            pos_c[x][y][num] = False
            arr[i][j] = 0
        if ok:
            return


if len(position):
    check(0)
else:
    for i in range(9):
        print(*arr[i])
