"""
https://www.acmicpc.net/problem/11404
"""
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e7)*+1

arr = [[INF]*n for _ in range(n)]
for i in range(n):
    arr[i][i] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    arr[a][b] = min(arr[a][b], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            cost = arr[i][k] + arr[k][j]
            if cost < arr[i][j]:
                arr[i][j] = cost

for i in range(n):
    for j in range(n):
        if arr[i][j] == INF:
            arr[i][j] = 0
    print(*arr[i])
