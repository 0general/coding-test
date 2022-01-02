"""
https://www.acmicpc.net/problem/16953
"""
# 기본 BFS 이용시 메모리 초과

A, B = map(int, input().split())
# A에서 B를 찾는 문제가 아닌 B에서 A를 찾는 문제로 바꾸자.

cnt = 1
while A <= B:
    if A == B:
        print(cnt)
        break
    if B % 2 == 0:
        B //= 2
    elif B % 10 == 1:  # 모든 홀수가 아닌 끝자리 1인 경우만 가능
        B //= 10
    else:
        print(-1)
        break
    if A > B:
        print(-1)
        break
    cnt += 1
