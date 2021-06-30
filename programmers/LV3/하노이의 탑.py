def move(n, mid, from_, to_, answer):
    if n == 1:
        answer.append([from_, to_])
        return
    move(n-1, to_, from_, mid, answer)
    answer.append([from_, to_])
    move(n-1, from_, mid, to_, answer)


def solution(n):
    answer = []
    move(n, 2, 1, 3, answer)
    return answer
