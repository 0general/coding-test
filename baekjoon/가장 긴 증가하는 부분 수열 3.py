"""
https://www.acmicpc.net/problem/12738
"""

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

ls = []

for num in arr:
    if len(ls) == 0:
        ls.append(num)
    else:
        if ls[-1] < num:
            ls.append(num)
            continue
        elif ls[-1] == num:
            continue
        s, e = 0, len(ls)-1
        ans = e
        while s <= e:
            mid = (s+e)//2
            if ls[mid] >= num:
                ans = mid
                e = mid - 1
            else:
                s = mid + 1
        ls[ans] = num

print(len(ls))
