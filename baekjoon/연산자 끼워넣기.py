"""
https://www.acmicpc.net/problem/14888
"""
import sys
from itertools import permutations


def plus(i):
    return temp + number[i]


def minus(i):
    return temp - number[i]


def multiple(i):
    return temp * number[i]


def divide(i):
    if temp < 0:
        return -(-temp // number[i])
    return temp // number[i]


input = sys.stdin.readline
op = ["+", "-", "*", "/"]
func = {"+": plus, "-": minus, "*": multiple, "/": divide}

# 숫자의 개수
n = int(input())
# 숫자
number = list(map(int, input().split()))
# 연산자별 개수
opn = list(map(int, input().split()))
oplist = []  # 모든 연산자를 담을 리스트

for i in range(4):
    oplist += [op[i]]*opn[i]

oplist = list(set(permutations(oplist, len(oplist))))

max = -10**9
min = 10**9
for o in oplist:
    temp = number[0]
    for i in range(1, n):
        temp = func[o[i-1]](i)
    if temp > max:
        max = temp
    if temp < min:
        min = temp

print(max)
print(min)
