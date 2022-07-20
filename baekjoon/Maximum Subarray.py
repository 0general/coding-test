"""
https://www.acmicpc.net/problem/10211
"""
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    x = arr[0]
    for i in range(1, n):
        arr[i] = max(arr[i], arr[i-1]+arr[i])
        x = max(x, arr[i])
    print(x)
