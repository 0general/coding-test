'''
https://www.acmicpc.net/problem/10989
'''
import sys
n = int(sys.stdin.readline())
arr = dict()
for _ in range(n):
    a = int(sys.stdin.readline())
    if a in arr:
        arr[a] += 1
    else:
        arr[a] = 1
arr = sorted(arr.items())

for i in arr:
    for _ in range(i[1]):
        print(i[0])
