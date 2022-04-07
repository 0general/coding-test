"""
https://www.acmicpc.net/problem/3806
"""
import sys

input = sys.stdin.readline

for i in range(1, int(input())+1):
    s = input().rstrip()
    t = input().rstrip()

    ans = 0
    o = 0
    z = 0
    q = 0  # ? 중 1과 바꿀 수 있는 것
    if len(s) != len(t):
        ans = -1
    else:
        for j in range(len(s)):
            if s[j] != t[j]:
                if s[j] == '?':
                    ans += 1
                    if t[j] == '1':
                        q += 1
                elif s[j] == '0':
                    z += 1
                else:
                    o += 1
        if o > z:  # s에서 불일치 한 것 중 1의 개수가 더 많을 때
            ans += z  # 0 과 1 교환
            o -= z  # 남은 1의 개수
            if o > q:  # q로 교환 불가
                ans = -1
            else:
                ans += o  # 남은
        else:  # s에서 0의 개수가 더 많거나 같을 때
            ans += o  # 0과 1 교환 횟수
            z -= o  # 남은 0의 개수
            ans += z  # 남은 0들 1로 바꿔줌

    print(f"Case {i}: {ans}")
