"""
https://www.acmicpc.net/problem/1715
"""
import heapq
import sys

input = sys.stdin.readline
n = int(input())
if n == 1:
    print(0)
else:
    h = []
    for _ in range(n):
        heapq.heappush(h, int(input()))
    cost = 0
    while len(h) > 1:
        a = h[0]
        heapq.heappop(h)
        a += h[0]
        heapq.heappop(h)
        cost += a
        heapq.heappush(h, a)

    print(cost)
