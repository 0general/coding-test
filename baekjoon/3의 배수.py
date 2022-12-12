"""
https://www.acmicpc.net/problem/1769
"""
import sys

input = sys.stdin.readline

x = input().rstrip()

num = 0
while True:
    if len(x) <= 1:
        x = int(x)
        break
    x = str(sum(map(int, list(x))))
    num += 1

print(num)
if x % 3 == 0:
    print("YES")
else:
    print("NO")
