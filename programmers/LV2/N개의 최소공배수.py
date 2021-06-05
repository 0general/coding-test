from math import gcd


def solution(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    answer = 1
    arr.sort()
    for i in range(n):
        answer = (answer*arr[i])//gcd(answer, arr[i])
    return answer
