"""
https://www.acmicpc.net/problem/2143
"""
import sys


def bs(num, findstart: bool):
    ans = -1
    s, e = 0, len(arrB)-1
    while s <= e:
        mid = (s+e)//2
        if arrB[mid] > num:
            e = mid - 1
        elif arrB[mid] < num:
            s = mid + 1
        else:
            ans = mid
            if findstart:
                e = mid - 1
            else:
                s = mid + 1
    return ans


t = int(input())
n = int(input())
arrA = list(map(int, input().split()))
m = int(input())
arrB = list(map(int, input().split()))

for i in range(1, n):
    arrA[i] += arrA[i-1]
    for j in range(i):
        arrA.append(arrA[i]-arrA[j])

for i in range(1, m):
    arrB[i] += arrB[i-1]
    for j in range(i):
        arrB.append(arrB[i]-arrB[j])

arrA.sort()
arrB.sort()

answer = 0
for a in arrA:
    num = t - a
    idx = bs(num, True)  # 첫 번째 인덱스
    if idx == -1:
        continue
    else:
        answer += bs(num, False) - idx + 1

print(answer)
