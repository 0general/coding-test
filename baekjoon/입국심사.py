"""
https://www.acmicpc.net/problem/3079
"""
import sys


def check(time, m):
    cnt = m
    for k in arr:
        cnt -= time//k
        if cnt <= 0:
            return True
    return False


input = sys.stdin.readline
n, m = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])


# 찾아야 하는 시간의 최솟값 t
l, r = arr[0], arr[-1]*m
t = r
while l <= r:
    mid = (l+r)//2
    if check(mid, m):
        t = mid
        r = mid - 1
    else:
        l = mid + 1
print(t)
