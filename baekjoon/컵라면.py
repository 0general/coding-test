"""
https://www.acmicpc.net/problem/1781
"""
import sys
import heapq

input = sys.stdin.readline

h = []
n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: (x[0], -x[1]))
for dline, gift in arr:
    if dline > len(h):
        heapq.heappush(h, gift)
    else:
        if h[0] < gift:
            heapq.heappop(h)
            heapq.heappush(h, gift)

print(sum(h))
