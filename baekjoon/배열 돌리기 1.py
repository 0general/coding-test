"""
https://www.acmicpc.net/problem/16926
"""
import sys
from math import gcd


def rotate(start):  # 한 칸 회전
    global dir
    visited[start][start] = True
    x, y = start, start
    change = graph[x][y]
    while True:
        nx, ny = x+dx[dir], y+dy[dir]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            temp = graph[nx][ny]
            graph[nx][ny] = change
            change = temp
            x, y = nx, ny
        else:
            dir = (dir + 1) % 4
            if dir == 0:
                graph[start][start] = change
                return


def visit(start):  # 껍데기 방문처리
    global dir
    visited[start][start] = True
    x, y = start, start
    while True:
        nx, ny = x+dx[dir], y+dy[dir]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            x, y = nx, ny
        else:
            dir = (dir + 1) % 4
            if dir == 0:
                return


input = sys.stdin.readline
# 배열 크기, 회전 수
n, m, r = map(int, input().split())
N, M = n, m
square = n*m
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]

husks = []  # 껍데기별 칸 수

dx = [1, 0, -1, 0]  # 아래, 오른쪽, 위쪽, 왼쪽
dy = [0, 1, 0, -1]

# 모든 껍데기가 제자리가 되는 최소 회전 수(r) 구하기

n -= 2
m -= 2
husks.append(square-n*m)
square = n*m
lcd = husks[0]  # 껍데기들의 최소공배수 구하기

while n > 2 and m > 2:  # 껍데기가 1 X A의 꼴이 되는 경우는 존재하지 않는다. -> 그러나 있어도 무방한 코드
    n -= 2
    m -= 2
    husks.append(square-n*m)
    square = n*m
    lcd = (husks[-1]*lcd)//gcd(lcd, husks[-1])

a = n*m
if a > 0:
    husks.append(a)
    lcd = (lcd*a)//gcd(lcd, a)

r %= lcd

dir = 0  # 초기 방향 = 아래쪽

visited = [[False]*M for _ in range(N)]
for i in range(len(husks)):  # 껍데기별로
    order = r % husks[i]
    for j in range(order):  # 각각 회전
        rotate(i)
    visit(i)  # 방문 처리

for i in range(len(graph)):
    print(*graph[i])
