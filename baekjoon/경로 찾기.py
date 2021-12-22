"""
https://www.acmicpc.net/problem/11403
"""
import sys

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for m in range(N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:  # 최단거리가 아닌 경로의 존재 여부니까
                continue
            if arr[i][m] and arr[m][j]:  # 마찬가지로 최단 거리가 아니니 존재 여부만 알고 있으면 된다.
                arr[i][j] = 1

for i in range(N):
    print(*arr[i])
