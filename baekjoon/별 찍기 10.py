"""
https://www.acmicpc.net/problem/2447
"""
import sys

input = sys.stdin.readline

N = int(input())

arr = [['*' for _ in range(N)] for _ in range(N)]
arr[1][1] = ' '


def iterate(k, x, y):
    for i in range(k):
        for j in range(k):
            arr[i+x*k][j+y*k] = arr[i][j]


def make_star(k):
    num = k // 3
    if num == 1:
        return
    make_star(num)  # base
    for x, y in [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]:
        iterate(num, x, y)
    for i in range(num, 2*num):
        for j in range(num, 2*num):
            arr[i][j] = ' '


make_star(N)

for i in range(N):
    print(''.join(arr[i]))
