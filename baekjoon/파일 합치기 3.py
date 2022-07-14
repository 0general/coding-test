"""
https://www.acmicpc.net/problem/13975
"""
import sys
import heapq
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    num = 0
    heapq.heapify(arr)
    while arr:
        x = heapq.heappop(arr) + heapq.heappop(arr)
        heapq.heappush(arr, x)
        num += x
        if len(arr) == 1:
            break
    print(num)
