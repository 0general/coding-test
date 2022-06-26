"""
https://www.acmicpc.net/problem/11003
"""
import sys
import heapq
input = sys.stdin.readline

N, L = map(int, input().split())
arr = list(map(int, input().split()))
h = []

for i in range(N):
    heapq.heappush(h, (arr[i], i))
    while h and i-L >= h[0][1]:
        heapq.heappop(h)
    print(h[0][0], end=' ')
