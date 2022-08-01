"""
https://www.acmicpc.net/problem/17609
"""
import sys
input = sys.stdin.readline


def check(s, i, j, count):
    if count >= 2:
        return count
    while i <= j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            # 어느쪽이든 유사회문이면 됨
            return min(check(s, i+1, j, count+1), check(s, i, j-1, count+1))
    return count


for _ in range(int(input())):
    s = input().rstrip()
    print(check(s, 0, len(s)-1, 0))
