# 명규의 마리오네트

def solution(numbers):
    answer = []
    for i in numbers:
        k = i + 1
        bit = bin(i ^ k)[2:]
        n = 0
        for j in bit:
            if j == '1':
                n += 1
        if n <= 2:
            answer.append(k)
        else:
            n -= 2
            answer.append(i+2**n)
    return answer
