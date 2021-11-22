"""
https://www.acmicpc.net/problem/2304
"""
import sys

input = sys.stdin.readline

# 기둥 개수 n
n = int(input())
arr = []
for _ in range(n):
    arr.append(tuple(map(int, input().split())))

arr.sort(key=lambda x: x[0])  # x좌표 크기 순으로 정렬
mx = 0
id = 0
for i in range(n):
    if arr[i][1] > mx:
        mx = arr[i][1]
        id = i

a = arr[0]
area = arr[id][1]  # 가장 높은 기둥 넓이를 더하고 시작

# 왼쪽부터 가장 높은 기둥의 왼쪽 벽까지 처리
for i in range(id):
    if arr[i+1][1] > a[1]:  # 왼쪽 벽을 만나면
        area += (arr[i+1][0]-a[0])*a[1]  # 가로 * 세로로 이전까지의 넓이 합 처리
        a = arr[i+1]  # 새로 구할 직사각형의 시작 저장

# 오른쪽부터 가장 높은 기둥의 오른쪽 벽까지 처리
a = arr[n-1]
for i in range(n-1, id, -1):
    if arr[i-1][1] >= a[1]:  # 기둥의 오른쪽 벽을 만나면 ###가장 높은 기둥이 여러 개일 수도 있으므로 부등호에 등호 추가
        area += (a[0]-arr[i-1][0])*a[1]
        a = arr[i-1]

print(area)
