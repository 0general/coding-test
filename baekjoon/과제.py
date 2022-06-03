"""
https://www.acmicpc.net/problem/13904
"""
import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: (x[0], -x[1]))
h = []
day = 0

for i in range(n):
    d, w = arr[i]
    if d > day:
        day += 1
        heapq.heappush(h, w)
    elif d == day and h[0] < w:
        heapq.heappop(h)
        heapq.heappush(h, w)

print(sum(h))
