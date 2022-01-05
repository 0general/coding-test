"""
https://www.acmicpc.net/problem/1629
"""
import sys

input = sys.stdin.readline
A, B, C = map(int, input().split())

A %= C


def mod_cal(a, b):
    if b == 1:
        return a % C

    a2 = mod_cal(a, b//2)
    a2 = (a2*a2) % C
    if b % 2 == 0:
        return a2
    else:
        return (a2*a) % C


answer = mod_cal(A, B)
print(answer)
