'''
https://www.acmicpc.net/problem/1759
'''


def BT(idx, num, letter):  # 검사 시작 위치 idx, 모음 수 num, 반환할 letter
    n = len(letter)
    if c-idx < l-n:
        return
    if n == l:
        if num >= 1 and l-num >= 2:
            print(letter)
        return
    if idx >= c:
        return
    if al[idx] in m:
        BT(idx+1, num+1, letter+al[idx])
    else:
        BT(idx+1, num, letter+al[idx])
    BT(idx+1, num, letter)


# answer = sorted(list(answer))
# for i in answer:
#     print(i)

# 비밀번호 자릿수, 문자 수
# l, c = map(int, input().split())
l, c = 4, 6
m = "aeiou"
# al = sorted(input().split())
al = ['a', 't', 'c', 'i', 's', 'w']
answer = set([])

BT(0, 0, "")
