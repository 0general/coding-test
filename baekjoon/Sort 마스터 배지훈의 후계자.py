"""
https://www.acmicpc.net/problem/20551
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()


def find(num):
    ans = -1
    s, e = 0, N-1
    while s <= e:
        mid = (s+e)//2
        if arr[mid] == num:
            ans = mid
            e = mid - 1
        elif arr[mid] > num:
            e = mid - 1
        else:
            s = mid + 1
    return ans


for _ in range(M):
    num = int(input())
    print(find(num))
