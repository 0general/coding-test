"""
https://www.acmicpc.net/problem/5430
"""
import sys
from collections import deque


def discard(arr, back):
    if len(arr) == 0:
        print('error')
        return False, back
    else:
        if not back:
            arr.popleft()
            return arr, back
        else:
            arr.pop()
            return arr, back


def reverse_arr(arr, back):
    return arr, not back


op = {'R': reverse_arr, 'D': discard}
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    back = False
    order = input().rstrip()
    num = int(input())
    ls = input().rstrip()
    if num > 0:
        arr = deque(ls[1:len(ls)-1].split(','))
    else:
        arr = deque()
    for i in range(len(order)):
        arr, back = op[order[i]](arr, back)
        if arr == False:
            break
    else:
        print('[', end='')
        if back:
            for i in range(len(arr)-1, -1, -1):
                if i == 0:
                    print(arr[i], end='')
                else:
                    print(arr[i], end=',')
        else:
            for i in range(len(arr)):
                if i == len(arr)-1:
                    print(arr[i], end='')
                else:
                    print(arr[i], end=',')
        print(']')
