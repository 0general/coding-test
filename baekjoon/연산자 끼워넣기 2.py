"""
https://www.acmicpc.net/problem/15658
"""
import sys


def plus(temp, i):
    return temp + number[i]


def minus(temp, i):
    return temp - number[i]


def multiple(temp, i):
    return temp * number[i]


def divide(temp, i):
    if temp < 0:
        return -(-temp // number[i])
    return temp // number[i]


def BT(idx, ans):  # 숫자 index, 현재까지 계산 결과
    global max, min
    if idx == n:
        if ans < min:
            min = ans
        if ans > max:
            max = ans
        return
    if idx > n:
        return
    for i in range(4):
        if opn[i] > 0:
            opn[i] -= 1
            BT(idx + 1, func[i](ans, idx))
            opn[i] += 1


func = {0: plus, 1: minus, 2: multiple, 3: divide}

input = sys.stdin.readline

n = int(input())  # 숫자 개수
number = list(map(int, input().split()))  # 피연산자
opn = list(map(int, input().split()))  # 연산자 개수 + - * / 순

max = -10**9
min = 10**9

BT(1, number[0])

print(max)
print(min)
