def solution(price, money, count):
    answer = money - (price * (1+count)*count/2)
    if answer < 0:
        return -answer

    return 0
