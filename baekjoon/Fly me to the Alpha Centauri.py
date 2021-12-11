"""
https://www.acmicpc.net/problem/1011
필독 : https://www.acmicpc.net/board/view/26059
"""
import sys
import math

input = sys.stdin.readline

for _ in range(int(input())):
    x, y = map(int, input().split())

    find = y-x
    s, e = 1, find
    num = 1
    while s <= e:
        mid = (s+e)//2
        if mid**2 <= find:
            s = mid + 1
            num = mid
        else:
            e = mid - 1
    a = num**2
    answer = num*2 - 1
    if a != find:
        answer += math.ceil((find-a)/num)
    print(answer)
