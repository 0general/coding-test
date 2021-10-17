"""
https://www.acmicpc.net/problem/1987
"""
import sys
input = sys.stdin.readline


def dfs(i, j, num):
    global length

    length = max(num, length)

    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if ((0 <= x < r) and (0 <= y < c)) and graph[x][y] not in al:
            al.add(graph[x][y])
            dfs(x, y, num + 1)
            al.remove(graph[x][y])


r, c = map(int, input().split())

graph = [list(input()) for _ in range(r)]
al = set()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

al.add(graph[0][0])
length = 1
dfs(0, 0, length)
print(length)

'''
12 16
ABCDEFGHIJKLMNOP
BCDEFGHIJKLMNOPQ
CDEFGHIJKLMNOPQR
DEFGHIJKLMNOPQRS
EFGHIJKLMNOPQRST
FGHIJKLMNOPQRSTU
GHIJKLMNOPQRSTUV
HIJKLMNOPQRSTUVW
IJKLMNOPQRSTUVWX
JKLMNOPQRSTUVWXY
KLMNOPQRSTUVWXYZ
LMNOPQRSTUVWXYZA
output : 26
시간 엄청 오래 걸림
좌표마다 들어갈 수 있는 값을 가지고 있는게 낫다.
dfs로는 시간 초과
'''
