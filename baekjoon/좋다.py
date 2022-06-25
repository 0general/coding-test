"""
https://www.acmicpc.net/problem/1253
"""
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 0
for i in range(N):
    s, e = 0, N-1
    while s < e:
        if s == i:
            s += 1
        if e == i:
            e -= 1
        if s >= e:
            break
        if arr[s] + arr[e] < arr[i]:
            s += 1
        elif arr[s] + arr[e] > arr[i]:
            e -= 1
        else:
            ans += 1
            break
print(ans)
