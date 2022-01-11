"""
https://www.acmicpc.net/problem/1713
"""
import sys


# 후보자가 이미 등록되어 있는지 확인
def check(x, i):
    if x in ans:
        increase_num(x)
    else:
        post_photo(x, i)


# 새로운 후보자 사진 게시
def post_photo(x, i):
    if len(ans) == n:
        d = find_minimum()
        del ans[d]
    ans[x] = [1, i]  # 추천 수 1, i번째로 추천받음


# 기존 후보자 추천 수 증가
def increase_num(x):
    ans[x][0] += 1


# 가장 적은 수의 추천자 찾기
def find_minimum():
    return min(ans.keys(), key=(lambda x: ans[x]))


input = sys.stdin.readline


n = int(input())
num = int(input())

rec = list(map(int, input().split()))
ans = {}

for i, p in enumerate(rec):
    check(p, i)

print(*sorted(ans.keys()))
