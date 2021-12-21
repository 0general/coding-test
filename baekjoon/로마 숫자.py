"""
https://www.acmicpc.net/problem/2608
"""
import sys


def to_int(string):
    answer = 0
    for i in range(len(string)):
        a = nums[string[i]]
        if i < len(string)-1 and a < nums[string[i+1]]:
            answer -= a
        else:
            answer += a
    return answer


def to_str(number):
    answer = ''
    for i in [1000, 100, 10, 1]:
        n = number//i
        if n > 0:
            if n <= 3:
                answer += rome[i]*n
            elif n <= 5:
                answer += rome[i*n]
            elif 6 <= n <= 8:
                answer += rome[i*5]
                answer += rome[i]*(n % 5)
            elif n == 9:
                answer += rome[i*n]
            number -= n*i
    return answer


nums = {'I': 1,	'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
rome = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
        90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}  # 4를 IX로 써서 엄청 틀렸다.

input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

num = to_int(str1) + to_int(str2)

print(num)
print(to_str(num))


'''
def str_to_int(string):
    answer = 0
    for i in range(len(string)):
        a = nums[string[i]]
        if i < len(string)-1 and a < nums[string[i+1]]:
            answer -= a
        else:
            answer += a
    return answer


def int_to_str(num):
    answer = ''
    for i in arab:
        while num >= i:
            answer += rome[i]
            num -= i

    return answer


nums = {'I': 1,	'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
arab = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
rome = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
        90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}

str1 = input().strip()
str2 = input().strip()

num = str_to_int(str1) + str_to_int(str2)

print(num)
print(int_to_str(num))
'''
