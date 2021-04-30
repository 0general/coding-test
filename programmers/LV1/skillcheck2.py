def solution(n):
    answer = []
    i = 0
    while 10**i < n:
        a = n % (10**(i+1))
        a = int(a/(10**i))
        anwer.append(a)
        i += 1
    return answer
