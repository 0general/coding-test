"""
https://www.acmicpc.net/problem/10800
"""
import sys

input = sys.stdin.readline

N = int(input())
color_acc = [0]*(N+1)  # 색깔별 누적 크기를 저장
weight_acc = [0]*(2001)  # 무게별 누적 무게를 저장
arr = []
ans = [0]*N
same = 0
total_sum = 0

for i in range(N):
    c, s = map(int, input().split())
    arr.append((c, s, i))

arr.sort(key=lambda x: (x[1], x[0]))

for i in range(N):  # 색상 별로 누적합
    c, s, idx = arr[i]
    total_sum += s  # 현재까지 총합
    color_acc[c] += s  # c 색상의 총합
    weight_acc[s] += 1  # s 사이즈의 총합
    if i != 0 and c == arr[i-1][0] and s == arr[i-1][1]:
        same += s
    else:
        same = s
    ans[idx] = total_sum - color_acc[c] - weight_acc[s]*s + same

for i in range(N):
    print(ans[i])
