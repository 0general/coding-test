def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer


# sum과 zip을 이용하면 for문이 없어도 된다.
# zip을 이용하자!
