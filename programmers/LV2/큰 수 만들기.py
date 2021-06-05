def solution(number, k):
    num = [number[0]]
    for i in number[1:]:
        while len(num) > 0 and num[-1] < i and k > 0:
            num.pop()
            k -= 1
        num.append(i)
    if k != 0:
        num = num[:-k]
    return "".join(num)
