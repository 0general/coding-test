"""
https://www.acmicpc.net/problem/1946
"""
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    ans = n
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort()
    mx = arr[0][1]
    for i in range(1, n):
        if arr[i][1] > mx:
            ans -= 1
        else:  # 통과
            mx = min(mx, arr[i][1])
    print(ans)
