"""
https://www.acmicpc.net/problem/2470
"""
import sys

input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
a, b = 0, 0
hap = 2*int(1e9)
flag = False
for i in range(0, n-1):
    s, e = i+1, n-1
    while s <= e:
        mid = (s+e)//2
        temp = abs(arr[i] + arr[mid])
        if arr[mid] == -arr[i]:
            a, b = i, mid
            flag = True
            break
        elif arr[mid] > -arr[i]:
            if temp < hap:
                a, b = i, mid
                hap = temp
            e = mid - 1
        else:
            if temp < hap:
                a, b = i, mid
                hap = temp
            s = mid + 1
    if flag:
        break

print(arr[a], arr[b])
