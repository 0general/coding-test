def solution(A, B):
    A.sort(reverse=True)
    B.sort()
    return [sum([i*j for i, j in zip(A, B)])][0]
