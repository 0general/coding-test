"""
https://www.acmicpc.net/problem/1654
"""
import sys
input = sys.stdin.readline
K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]
s, e = 1, max(arr)  # 반드시 1보다 큰 수

ans = 0
while s <= e:
    mid = (s+e)//2  # zerodivision 피하기 위해 s = 1로 설정
    temp = 0
    for leng in arr:
        temp += leng//mid
    if temp < N:
        e = mid - 1
    else:
        ans = mid
        s = mid + 1

print(ans)
