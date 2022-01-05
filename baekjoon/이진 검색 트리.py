"""
https://www.acmicpc.net/problem/5639
"""
# 입력 종료는 Ctrl + Z

import sys


def find_sub(start, end):
    if start > end:
        return
    if start == end:
        print(tree[start])
        return
    s, e = start+1, end
    ans = start  # 왼쪽 서브 트리의 끝 노드 인덱스를 저장할 변수
    while s <= e:
        mid = (s+e)//2
        if tree[mid] <= tree[start]:
            ans = mid
            s = mid + 1
        else:
            e = mid - 1
    find_sub(start+1, ans)
    find_sub(ans+1, end)
    print(tree[start])


input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))  # 너무 크게 잡으면 메모리 초과
tree = []

while True:
    try:
        i = int(input())
    except:
        break
    tree.append(i)

find_sub(0, len(tree)-1)
