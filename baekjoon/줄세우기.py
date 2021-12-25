"""
https://www.acmicpc.net/problem/2631
lIS 가장 긴 증가하는 부분 수열의 길이를 구해서 전체 길이에서 빼준다.
"""
import sys

input = sys.stdin.readline

n = int(input())
ls = []
for _ in range(n):
    num = int(input())
    if len(ls) == 0:
        ls.append(num)
    else:
        if ls[-1] < num:
            ls.append(num)
        else:
            s, e = 0, len(ls)-1
            ans = 0
            while s <= e:
                mid = (s+e)//2
                if ls[mid] >= num:
                    ans = mid
                    e = mid - 1
                else:
                    s = mid + 1
            ls[ans] = num

print(n-len(ls))
