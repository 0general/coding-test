"""
https://www.acmicpc.net/problem/2467
"""
import sys


def binary_search(sidx):
    global ans
    global stop
    s, e = sidx+1, n-1
    while s <= e:
        mid = (s+e)//2
        temp = arr[sidx]+arr[mid]
        if temp == 0:
            ans = [arr[sidx], arr[mid]]
            stop = True
            return
        if abs(temp) < abs(sum(ans)):
            ans = [arr[sidx], arr[mid]]
        if temp > 0:
            e = mid - 1
        else:
            s = mid + 1
    return


input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

ans = [arr[0], arr[1]]
stop = False
for i in range(n-1):
    if arr[i] > abs(sum(ans)):
        break
    binary_search(i)
    if stop:
        break

print(*ans)
