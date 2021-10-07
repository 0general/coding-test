"""
https://www.acmicpc.net/problem/2263
"""
import sys


def find_index(si, ei, v):
    for i in range(ei-si+1):
        if vin[si+i] == v:
            return i


def find_root(si, ei, ps, pe):  # 인오더, 포스트오더
    if si > ei:
        return
    if si == ei:
        print(vin[si], end=' ')
        return
    v = post[pe]
    print(v, end=' ')

    ix = find_index(si, ei, v)
    find_root(si, si+ix-1, ps, ps+ix-1)
    find_root(si+ix+1, ei, ps+ix, pe-1)


input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())

vin = list(map(int, input().split()))
post = list(map(int, input().split()))


s = 0
e = len(vin)-1
find_root(s, e, s, e)
