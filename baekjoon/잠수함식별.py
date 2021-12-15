"""
https://www.acmicpc.net/problem/2671
"""
import sys
import re

input = sys.stdin.readline

p = re.compile('(100+1+|01)+')
if p.fullmatch(input().rstrip()):  # 패턴과 문자열이 남는 부분 없이 완벽하게 일치하는지를 검사
    print("SUBMARINE")
else:
    print("NOISE")
