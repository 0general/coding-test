"""
https://www.acmicpc.net/problem/12919
"""
import sys
from collections import deque


def remove_A(arr):
    arr.pop()
    if len(arr) == s:
        return check(arr)
    q.append(arr)
    return False


def remove_B(arr):
    arr = arr[1:]
    arr.reverse()
    if len(arr) == s:
        return check(arr)
    q.append(arr)
    return False


def check(arr):
    global ans
    for i, j in zip(arr, S):
        if i != j:
            return False
    ans = 1
    return True


input = sys.stdin.readline
S = list(input().rstrip())
T = list(input().rstrip())
s = len(S)
q = deque()
q.append(T)
ans = 0

while q:
    now = q.popleft()
    if now[0] == 'B':
        remove_B(now)
    if now[-1] == 'A':
        remove_A(now)
    if ans:
        break

print(ans)
