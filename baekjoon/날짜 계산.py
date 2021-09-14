'''
https://www.acmicpc.net/problem/1476
'''
E, S, M = map(int, input().split())

# 가장 숫자 범위가 큰 S로 검사
i = 0
while True:
    # 검사할 숫자
    num = (28 * i) + S
    if M == 19:
        m = 0
    else:
        m = M
    if E == 15:
        e = 0
    else:
        e = E
    if num % 19 == m and num % 15 == e:
        print(num)
        break
    i += 1
