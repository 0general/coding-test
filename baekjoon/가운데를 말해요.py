"""
https://www.acmicpc.net/problem/1655
"""
import sys
import heapq
input = sys.stdin.readline


n = int(input())
left = []
right = []


def median():
    x = int(input())

    if len(left) == 0:
        heapq.heappush(left, -x)  # 최대힙
        return x
    if len(left) > len(right):
        heapq.heappush(left, -x)
        heapq.heappush(right, -heapq.heappop(left))
        return -left[0]
    else:
        heapq.heappush(right, x)
        heapq.heappush(left, -heapq.heappop(right))
        return -left[0]


for _ in range(n):
    print(median())
