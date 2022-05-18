"""
https://www.acmicpc.net/problem/1114
"""
import sys

input = sys.stdin.readline

L, K, C = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()


def check(size):
    x = L
    num = 0
    i = K-1
    while i >= 0:
        if num < C:
            if x - arr[i] > size:
                if i == K-1:
                    return -1
                x = arr[i+1]
                num += 1
                continue
            elif x - arr[i] == size:
                x = arr[i]
                num += 1
        elif num == C:
            if x > size:
                return -1
            else:
                return x
        i -= 1

    if arr[0] <= size:
        return arr[0]
    else:
        return -1


s, e = 0, L
leng = L
loc = L
while s <= e:
    mid = (s+e)//2
    ans = check(mid)
    if ans < 0:
        s = mid + 1
    else:
        leng = mid
        loc = ans
        e = mid - 1

print(leng, loc)
