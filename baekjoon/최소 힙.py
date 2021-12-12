"""
https://www.acmicpc.net/problem/1927
"""
import sys
import heapq

input = sys.stdin.readline
h = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        if len(h) == 0:
            print(0)
            continue
        else:
            print(heapq.heappop(h))
            continue
    else:
        heapq.heappush(h, x)
