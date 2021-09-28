"""
https://www.acmicpc.net/problem/10828
"""
import sys
input = sys.stdin.readline


def push():
    n = int(do[1])
    stack.append(n)


def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])


def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)


def size():
    print(len(stack))


def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack.pop())


order = {"push": push, "top": top, "empty": empty, "size": size, "pop": pop}
stack = []

t = int(input())
for _ in range(t):
    do = input().split()
    order[do[0]]()
