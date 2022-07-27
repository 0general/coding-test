"""
https://www.acmicpc.net/problem/19637
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
name = []
power = []
for _ in range(n):
    a, b = input().rstrip().split()
    name.append(a)
    power.append(int(b))

for _ in range(m):
    x = int(input())
    s, e = 0, n-1
    ans = 0
    while s <= e:
        mid = (s+e)//2
        if x > power[mid]:
            s = mid + 1
        else:
            ans = mid
            e = mid - 1
    print(name[ans])
