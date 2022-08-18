"""
https://www.acmicpc.net/problem/11729
"""
import sys
input = sys.stdin.readline

N = int(input())
ans = 0
ls = []


def hanoi(n, start, mid, target):
    global ans
    if n == 1:
        ans += 1
        ls.append(f"{start} {target}")
        return
    hanoi(n-1, start, target, mid)
    ls.append(f"{start} {target}")
    ans += 1
    hanoi(n-1, mid, start, target)


hanoi(N, 1, 2, 3)
print(ans)
for s in ls:
    print(s)
