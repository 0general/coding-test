"""
https://www.acmicpc.net/problem/9342
"""
import sys
import re

input = sys.stdin.readline
p = re.compile('^[A-F]?A+F+C+[A-E]?$')

for _ in range(int(input())):
    print('Good' if p.match(input().rstrip()) == None else 'Infected!')
