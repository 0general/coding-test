"""
https://www.acmicpc.net/problem/18258
"""
import sys
from collections import deque

input = sys.stdin.readline
q = deque()

for _ in range(int(input())):
    order_list = list(input().split())
    if order_list[0] == "push":
        q.append(int(order_list[1]))
    elif order_list[0] == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif order_list[0] == "size":
        print(len(q))
    elif order_list[0] == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif order_list[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)
