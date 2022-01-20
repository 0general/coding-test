"""
https://www.acmicpc.net/problem/9019

반드시 읽어야 할 조건 해석 관련 글
https://www.acmicpc.net/board/view/54644
"""
import sys
from collections import deque

input = sys.stdin.readline


def D(num):
    return (num*2) % 10000, 'D'


def S(num):
    return (num-1) % 10000, 'S'


def L(num):  # 1 은 10이 된다. 0으로 패딩되어있다고 생각하면 됨.
    num = str(num)
    num = (4-len(num))*'0'+num
    num = num[1:]+num[0]
    return int(num), 'L'


def R(num):  # 1은 1000이 된다.
    num = str(num)
    num = (4-len(num))*'0'+num
    num = num[-1]+num[:-1]
    return int(num), 'R'


def bfs():
    while q:
        num = q.popleft()
        for i, x in [D(num), S(num), L(num), R(num)]:
            if arr[i] == '_':
                arr[i] = arr[num]+x
                if i == B:
                    return
                q.append(i)


for _ in range(int(input())):
    arr = ['_' for _ in range(10000)]
    A, B = map(int, input().split())
    arr[A] = ''
    q = deque()
    q.append(A)
    bfs()
    print(arr[B])
