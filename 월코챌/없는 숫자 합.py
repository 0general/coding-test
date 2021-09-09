# 0~9까지의 숫자로 이루어진 numbers 리스트가 주어졌을 때 리스트에 존재하지 않는 숫자들을 더해서 리턴

def solution(numbers):
    return 45-sum(set(numbers))
