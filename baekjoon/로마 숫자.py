"""
https://www.acmicpc.net/problem/2608
"""


def str_to_int(string):
    answer = 0
    hap = 0
    last = ''
    for s in string:
        if last == '':
            last = s
            hap = nums[last]
        else:
            if nums[last] > nums[s]:
                last = s
                answer += hap
                hap = nums[s]
            elif nums[last] == nums[s]:
                hap += nums[s]
            else:
                answer -= hap
                hap = nums[s]
                last = s
    answer += hap
    return answer


def int_to_str(num):
    answer = ''
    for i in [1000, 100, 10, 1]:
        n = num//i
        if n <= 3:
            answer += strings[i]*n
        elif n == 4:
            answer += strings[i]
            answer += strings[i*5]
        elif n == 5:
            answer += strings[i*5]
        elif 6 <= n <= 7:
            answer += strings[i*5]
            answer += strings[i]*(n-1)
        elif n >= 8:
            answer += strings[i]*(10-n)
            answer += strings[i*10]
        num -= n*i
    return answer


nums = {'I': 1,	'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
strings = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

str1 = input()
str2 = input()

num = str_to_int(str1) + str_to_int(str2)

print(num)
print(int_to_str(num))
