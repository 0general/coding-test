"""
https://www.acmicpc.net/problem/1477
"""
import sys

input = sys.stdin.readline
N, M, L = map(int, input().split())
arr = [0]+sorted(list(map(int, input().split())))+[L]

length = []
for i in range(1, N+2):
    length.append(arr[i]-arr[i-1])  # N이 1일 때까지도 고려한 코드

length.sort()  # 총 길이 N+1


def check(minimum):
    x = 0
    for l in length:
        x += (l-1)//minimum  # 나누어떨어지는 경우를 고려해서 -1을 넣는다.
        if x > M:
            return False
    return True


s, e = 1, length[-1]
ans = e
while s <= e:
    mid = (s+e)//2  # 최소값
    if check(mid):
        ans = mid
        e = mid - 1
    else:
        s = mid + 1

print(ans)
