"""
https://www.acmicpc.net/problem/1149
"""
import sys
input = sys.stdin.readline

ans = [0, 0, 0]  # 마지막 집이 빨강, 초록, 파랑으로 칠해질 때의 최소 비용
# 사용하는 건 바로 이전 집까지의 결정된 비용이므로 배열의 길이가 길 필요가 없다.

for i in range(int(input())):
    temp = list(map(int, input().rstrip().split()))
    temp[0] += min(ans[1], ans[2])
    temp[1] += min(ans[0], ans[2])
    temp[2] += min(ans[0], ans[1])
    ans = temp

print(min(ans))
