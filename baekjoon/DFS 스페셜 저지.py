"""
https://www.acmicpc.net/problem/16964
"""
from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
arr = defaultdict(bool)
for _ in range(N-1):
    a, b = map(int, input().split())
    arr[(a, b)] = True
    arr[(b, a)] = True

check = list(map(int, input().split()))
stack = [1]

if check[0] != 1:
    print(0)
else:
    for i in range(1, N):
        ok = False
        while stack:
            if arr[(stack[-1], check[i])]:
                stack.append(check[i])
                ok = True
                break
            stack.pop()
        if not ok:
            print(0)
            break
    else:
        print(1)
