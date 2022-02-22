"""
https://www.acmicpc.net/problem/15662
"""
import sys
from collections import deque

input = sys.stdin.readline


def chain_rotate(idx, dir, right, left):
    a = gear[idx][2]  # 톱니바퀴 회전 전 3시 방향 극 확인
    b = gear[idx][6]  # 톱니바퀴 회전 전 9시 방향 극 확인
    gear[idx].rotate(dir)
    if right and idx + 1 <= T and a != gear[idx+1][6]:
        chain_rotate(idx+1, -dir, right, False)
    if left and idx - 1 > 0 and b != gear[idx-1][2]:
        chain_rotate(idx-1, -dir, False, left)


T = int(input())
gear = [[] for _ in range(T+1)]
for i in range(1, T+1):
    gear[i] = deque(map(int, list(input().rstrip())))

for _ in range(int(input())):
    idx, dir = map(int, input().split())
    chain_rotate(idx, dir, True, True)


ans = 0
for i in range(1, T+1):
    if gear[i][0] == 1:  # S극
        ans += 1

print(ans)
