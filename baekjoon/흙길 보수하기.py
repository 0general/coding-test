"""
https://www.acmicpc.net/problem/1911
"""
# 간단한 스위핑
# 스위핑 알고리즘의 정의를 다시 정리하고
import sys

input = sys.stdin.readline

n, l = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: x[0])

cnt = 0
start = 0

for s, e in arr:
    if start > e:
        continue
    else:
        if start < s:
            start = s
        while start < e:  # 여기 줄일 것
            cnt += 1
            start += l

print(cnt)
