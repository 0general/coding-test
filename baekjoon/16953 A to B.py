"""
https://www.acmicpc.net/problem/16953
"""
# BFS로도 가능, 아래에 코드 확인

A, B = map(int, input().split())
# A에서 B를 찾는 문제가 아닌 B에서 A를 찾는 문제로 바꾸자.

cnt = 1
while A <= B:
    if A == B:
        print(cnt)
        break
    if B % 2 == 0:
        B //= 2
    elif B % 10 == 1:  # 모든 홀수가 아닌 끝자리 1인 경우만 가능
        B //= 10
    else:
        print(-1)
        break
    if A > B:
        print(-1)
        break
    cnt += 1


'''
import sys
from collections import deque


def bfs(a, b):
    q = deque()
    q.append((a, 1))
    while q:
        n, t = q.popleft()
        for m in [2*n, int(str(n)+"1")]:
            if m <= b:
                if m == b:
                    return t+1
                q.append((m, t+1))
    return -1


input = sys.stdin.readline

a, b = map(int, input().split())

print(bfs(a, b))


# visited 없어도 됨. 
# visited = [False]*(b+1) 하나 했다가 메모리 초과 엄청났지만, 
# 그거 없애니까 통과됨.
'''
