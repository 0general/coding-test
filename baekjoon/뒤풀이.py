"""
https://www.acmicpc.net/problem/14575
"""
import sys

input = sys.stdin.readline

n, total = map(int, input().split())
arr = []
s, e = 1, 1
ok = 0  # 모두 L이상은 먹을 수 있어야 하므로 확인 작업
for _ in range(n):
    l, r = map(int, input().split())
    s = max(s, l)
    e = max(e, r)
    arr.append((l, r))
    ok += l

ans = -1


def check(S):
    global arr, total
    extra = 0
    for l, r in arr:
        extra += min(S, r)  # 모두 L 이상 먹고 남은 양을 나눠 마실 수 있는지 합산
        if extra >= total:
            return True
    return False


if total >= ok:
    while s <= e:
        mid = (s+e)//2
        if check(mid):
            ans = mid
            e = mid - 1
        else:
            s = mid + 1

print(ans)
