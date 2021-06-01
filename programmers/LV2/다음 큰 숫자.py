def solution(n):
    k = n+1
    while True:
        if bin(k).count("1") == bin(n).count("1"):
            return k
        k += 1
