"""
https://www.acmicpc.net/problem/2473
"""
# 시간 복잡도 O(N²)
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
mini = 3*int(1e9)+1
l, m, r = 0, 0, 0
for i in range(n-2):
    for j in range(i+1, n-1):
        temp = arr[i]+arr[j]
        s, e = j+1, n-1
        while s <= e:
            mid = (s+e)//2
            t = abs(temp+arr[mid])
            if arr[mid] == -temp:
                mini = 0
                l, m, r = i, j, mid
                break
            elif arr[mid] < -temp:
                if t < mini:
                    l, m, r = i, j, mid
                    mini = t
                s = mid + 1
            else:
                if t < mini:
                    l, m, r = i, j, mid
                    mini = t
                e = mid - 1
        if mini == 0:
            break
    if mini == 0:
        break

print(arr[l], arr[m], arr[r])
