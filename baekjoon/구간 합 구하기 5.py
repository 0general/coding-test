"""
https://www.acmicpc.net/problem/11660
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [[0]*(N+1)]
for _ in range(N):
    arr.append([0]+list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, N+1):
        # arr[i][j]에 arr[1][1]과 arr[i][j]를 대각꼭짓점으로 가지는 직사각형 내부의 합을 저장해둔다.
        arr[i][j] += arr[i][j-1] + arr[i-1][j] - arr[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    answer = arr[x2][y2]-arr[x1-1][y2]-arr[x2][y1-1]+arr[x1-1][y1-1]
    print(answer)
