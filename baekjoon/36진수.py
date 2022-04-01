"""
https://www.acmicpc.net/problem/1036
"""
import sys

input = sys.stdin.readline

n = int(input())
num = [[0, i] for i in range(36)]
for _ in range(n):
    string = input().rstrip()
    i = 0
    for s in string[::-1]:
        s = ord(s)
        if s < 65:
            s -= 48
        else:
            s -= 55
        num[s][0] += 36**i  # 숫자
        i += 1

k = int(input())
num.sort(key=lambda x: (-x[0]*(35-x[1]), -x[0])) #변화량을 기준으로 정렬해야한다.
answer = 0
for i in range(36):
    if num[i][0] == 0:
        break
    if k != 0:
        answer += num[i][0]*35
        k -= 1
    else:
        answer += num[i][0]*num[i][1]

number = ''
while answer != 0:
    s = answer % 36
    if s >= 10:
        s += 55
        s = chr(s)
    number += str(s)
    answer //= 36

if number == '':
    print(0)
else:
    print(number[::-1])
