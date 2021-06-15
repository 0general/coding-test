def solution(n):
    if n < 3:
        return 1
    num = n//2 if n % 2 == 0 else n//2 + 1
    l = list(range(num, 0, -1))
    win = 2
    answer = 0
    i = 0
    while True:
        if i+win > len(l):
            break
        if sum(l[i:i+win]) == n:
            answer += 1
            i += 1
        elif sum(l[i:i+win]) < n:
            win += 1
            continue
        else:
            i += 1
            continue
    return answer + 1
