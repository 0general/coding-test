"""
https://www.acmicpc.net/problem/16172
"""
import sys
import re

input = sys.stdin.readline
sys.setrecursionlimit(200000)
string = input().rstrip()

target = input().rstrip()

string = "".join(re.findall('[a-zA-Z]+', string))

if re.search(target, string):
    print(1)
else:
    print(0)
