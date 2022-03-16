"""
https://www.acmicpc.net/problem/2162
"""
import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
parent = [i for i in range(n)]
arr = [list(map(int, input().split())) for _ in range(n)]

# ccw(counter clockwise) 이용 - 양수 나오면 반시계


def ccw(p1, p2, p3):
    num = (p3[0]-p1[0])*(p2[1]-p1[1]) - (p3[1]-p1[1])*(p2[0]-p1[0])
    if num < 0:
        return -1
    elif num == 0:
        return 0
    else:
        return 1


def iscross(p1, p2, p3, p4):
    num1 = ccw(p1, p2, p3)*ccw(p1, p2, p4)
    num2 = ccw(p3, p4, p1)*ccw(p3, p4, p2)
    if num1 == 0 and num2 == 0:  # 선분이 일직선 상에 있는 경우
        if not issort(p1, p2):
            p1, p2 = swap(p1, p2)
        if not issort(p3, p4):
            p3, p4 = swap(p3, p4)
        return (issort(p3, p2) and issort(p1, p4))
    elif num1 <= 0 and num2 <= 0:  # 하나라도 양수가 나온다면 교차하지 않음
        return True
    else:
        return False


def swap(p, q):
    p[0], q[0] = q[0], p[0]
    p[1], q[1] = q[1], p[1]
    return p, q


def issort(p, q):
    if p[0] == q[0]:
        return p[1] <= q[1]
    else:
        return p[0] < q[0]


def find_parent(x):
    global parent
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    global parent
    a = find_parent(a)
    b = find_parent(b)
    if a == b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(n-1):
    for j in range(i, n):
        if find_parent(i) == find_parent(j):
            continue
        if iscross(arr[i][0:2], arr[i][2:], arr[j][0:2], arr[j][2:]):
            union_parent(i, j)

for i in range(n):
    find_parent(i)

c = Counter(parent)
print(len(c))
print(c.most_common(1)[0][1])
