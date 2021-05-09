def solution(n):
    answer = 0
    list = []
    while n//3 >= 0:
        if n//3 == 0:
            list.append(n % 3)
            break
        else:
            list.append(n % 3)
            n //= 3
    list.reverse()
    for i, j in enumerate(list):
        answer += j*(3**i)
    return answer
