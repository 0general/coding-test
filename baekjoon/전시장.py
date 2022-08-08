"""
https://www.acmicpc.net/problem/2515
"""
import sys

input = sys.stdin.readline

N, S = map(int, input().split())
drawing = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(N)]
drawing.sort(key=lambda x: (x[0], -x[1]))  # 낮고 가격 높은 순 정렬
dp = [0]*(N+1)  # i번째 그림까지 고려했을 때 얻을 수 있는 최대 그림 값
if drawing[0][0] >= S:
    dp[0] = drawing[0][1]

prev = [0 for _ in range(N+1)] # 이전 그림 중에 길이가 S이상 차이나는 마지막 그림의 인덱스 
for i in range(1, N+1):
    temp = prev[i-1]
    s, e = prev[i-1], i - 1
    while s <= e:
        mid = (s+e)//2
        if drawing[i][0]-drawing[mid][0] >= S:
            temp = mid
            s = mid + 1
        else:
            e = mid - 1
    prev[i] = temp


for i in range(1, N+1):
    dp[i] = max(drawing[i][1], dp[prev[i]]+drawing[i][1], dp[i-1])

print(dp[N])
