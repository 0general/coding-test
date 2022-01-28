"""
https://www.acmicpc.net/problem/12904
"""
import sys


def delete_B():
    global T
    T.pop()
    T.reverse()
    return


def delete_A():
    global T
    T.pop()
    return


input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

while len(S) < len(T):
    if T[-1] == 'B':
        delete_B()
    else:
        delete_A()

for i, j in zip(S, T):
    if i != j:
        print(0)
        break
else:
    print(1)
