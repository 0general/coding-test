def solution(n):
    num = {0: '4', 1: '1', 2: '2'}
    answer = ''
    while n > 0:
        k = n % 3
        if k == 0:
            n = n//3 - 1
        else:
            n //= 3
        answer += num[k]

    return "".join(reversed(answer))
