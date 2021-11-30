"""
https://www.acmicpc.net/problem/12015
pypy3 로 채점해야 시간 초과가 안 난다.
"""
import sys

input = sys.stdin.readline

# 수열의 길이
n = int(input())
arr = list(map(int, input().rstrip().split()))
ls = []

for i in range(n):
    if len(ls) == 0:
        ls.append(arr[i])
    else:
        if arr[i] > ls[-1]:
            ls.append(arr[i])
            continue
        elif arr[i] == ls[-1]:
            continue
        else:
            ans = len(ls)-1
            s, e = 0, ans
            while s <= e:
                mid = (s+e)//2
                if ls[mid] >= arr[i]:
                    ans = mid
                    e = mid-1
                else:
                    s = mid+1
            ls[ans] = arr[i]

print(len(ls))
