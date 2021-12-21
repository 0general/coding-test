"""
https://www.acmicpc.net/problem/18428
"""
import sys
from itertools import combinations as comb


def check():  # 학생들이 안 걸릴 수 있는지 check
    for s in teacher:
        x, y = s
        for i in range(4):
            tx, ty = x, y
            while True:
                nx, ny = tx+dx[i], ty+dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if arr[nx][ny] == 'S':
                        return False
                    elif arr[nx][ny] == 'O':
                        break
                    tx, ty = nx, ny
                else:
                    break
    return True


input = sys.stdin.readline

n = int(input())
arr = []
teacher = []
hway = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    arr.append(list(input().rstrip().split()))
    for j in range(n):
        if arr[i][j] == 'T':
            teacher.append((i, j))
        elif arr[i][j] == 'X':
            hway.append((i, j))

for ls in list(comb(hway, 3)):
    for x, y in ls:
        arr[x][y] = 'O'
    if check():
        print("YES")
        break
    for x, y in ls:
        arr[x][y] = 'X'
else:
    print("NO")
