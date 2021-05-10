def solution(n):
    return "수박"*(n//2) + "수"*(n % 2)


def solution2(n):
    return "".join(["수" if i % 2 == 0 else "박" for i in range(n)])
