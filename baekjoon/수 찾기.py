"""
https://www.acmicpc.net/problem/1920
"""
import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
M = int(input())
for num in list(map(int, input().split())):
    s, e = 0, N-1
    ans = 0
    while s <= e:
        mid = (s+e)//2
        if arr[mid] == num:
            ans = 1
            break
        elif arr[mid] > num:
            e = mid - 1
        else:
            s = mid + 1
    print(ans)
