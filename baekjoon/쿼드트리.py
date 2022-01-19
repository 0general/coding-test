"""
https://www.acmicpc.net/problem/1992
"""
import sys


def div_conq(sx, sy, size):
    if size == 1:
        return arr[sx][sy]
    next = size//2
    s = div_conq(sx, sy, next) + div_conq(sx, sy+next, next) + \
        div_conq(sx+next, sy, next) + div_conq(sx+next, sy+next, next)
    if s == '0000':
        return '0'
    elif s == '1111':
        return '1'
    else:
        return '('+s+')'


input = sys.stdin.readline

n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]

print(div_conq(0, 0, n))
