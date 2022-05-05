"""
https://www.acmicpc.net/problem/2805
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

s, e = 0, arr[-1]
h = 0
while s <= e:
    mid = (s+e)//2
    temp = 0
    for t in arr:
        temp += max(0, t-mid)
        if temp >= M:
            break
    if temp < M:
        e = mid - 1
    else:
        h = mid
        s = mid + 1

print(h)
