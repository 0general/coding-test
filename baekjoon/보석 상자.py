"""
https://www.acmicpc.net/problem/2792
"""
import sys
import math
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(M)]


def check(val):  # check 함수가 시간 복잡도에 크게 영향을 끼친다. N은 10억, M은 30만이므로 M에 맞춰서 작성
    x = 0
    for num in arr:
        x += math.ceil(num/val)
        if x > N:
            return False
    return True


s, e = 1, int(1e9)
ans = e

while s <= e:
    mid = (s+e)//2
    if check(mid):
        ans = mid
        e = mid - 1
    else:
        s = mid + 1

print(ans)
