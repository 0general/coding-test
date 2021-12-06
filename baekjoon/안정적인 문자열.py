"""
https://www.acmicpc.net/problem/4889
stack 자료구조 이용. 굳이 stack을 구현할 필요없이 LIFO의 성질만을 이용했다.
"""
import sys

input = sys.stdin.readline
num = 1
while True:
    open = 0  # 남은 여는 괄호의 개수
    temp = 0
    arr = list(input().rstrip())
    if arr[0] == '-':
        break
    for i in range(len(arr)):
        if arr[i] == '{':
            open += 1
        else:
            if open == 0:
                temp += 1  # 여는 괄호없이 만난 닫는 괄호의 개수
                open += 1  # 여는 괄호로 변환
            else:
                open -= 1
    print(f"{num}. {open//2 + temp}")  # 여는 괄호의 절반 변환 + 변환 횟수
    num += 1

'''
{{{}{}}{
{{{{
{}{{
}}}}
}{{}
}}{}
}}{{
---
1. 1
2. 2
3. 1
4. 2
5. 2
6. 1
7. 2



{{{}}}
{{}}
{}{{}}
{}{}{}{}{}{}
{}{}{{
{}{}}}
{}{}{}{}{}{}{}}}}}{{{{
}}}{{{
}}}{
---
1. 0
2. 0
3. 0
4. 0
5. 1
6. 1
7. 4
8. 4
9. 3
'''
