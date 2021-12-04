"""
https://www.acmicpc.net/problem/2075
"""
import heapq
import sys

input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))
heapq.heapify(h)
for i in range(1, n):
    a = list(map(int, input().split()))
    for num in a:
        if h[0] < num:
            heapq.heappop(h)
            heapq.heappush(h, num)

print(h[0])
