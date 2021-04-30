def solution(prices):
    answer = []
    n = len(prices)
    for i in range(n):
        time = 0
        j = i
        minor = prices[i]
        while minor <= prices[j]:
            j += 1
            if j == n:
                break
            else:
                time += 1
        answer.append(time)
    return answer
