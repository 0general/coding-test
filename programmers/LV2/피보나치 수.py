def solution(n):
    answer = [0, 1]
    i = 1
    while i < n:
        i += 1
        answer.append(answer[-1] + answer[-2])
    return answer[-1] % 1234567
