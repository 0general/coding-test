"""
https://www.acmicpc.net/problem/14391
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]


ans = 0

for k in range(1 << n*m):  # 모든 칸에서 가로로 갈지 세로로 갈지 선택 가능 2^(n*m) 가짓수를 모두 살펴봐야함
    sum = 0
    for i in range(n):  # 가로 방향 합산 구하기
        line = 0
        for j in range(m):
            num = i*m + j
            if k & (1 << num):
                sum += line
                line = 0
            else:
                line = line*10 + arr[i][j]
        sum += line

    for i in range(m):  # 세로 방향 합산 구하기
        line = 0
        for j in range(n):
            num = j*m + i
            if k & (1 << num):
                line = line*10 + arr[j][i]
            else:
                sum += line
                line = 0
        sum += line

    ans = max(ans, sum)

print(ans)
