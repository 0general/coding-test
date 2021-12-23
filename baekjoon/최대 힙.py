"""
https://www.acmicpc.net/problem/11279
"""
import heapq
import sys

input = sys.stdin.readline

N = int(input())
h = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if len(h) == 0:
            print(0)
        else:
            print(-heapq.heappop(h))
    else:
        heapq.heappush(h, -x)
