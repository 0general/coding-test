"""
https://www.acmicpc.net/problem/16916
"""
import re
import sys

input = sys.stdin.readline

whole = input().rstrip()
part = input().rstrip()

if re.search(part, whole) is not None:  # search는 중간부분에서도 찾는다 <-> match는 첫번째 위치에서 없으면 None
    print(1)
else:
    print(0)
