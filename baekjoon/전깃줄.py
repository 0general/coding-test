"""
https://www.acmicpc.net/problem/2565
"""
import sys

input = sys.stdin.readline
# 전깃줄 개수
n = int(input())
arr = []
for _ in range(n):
    arr.append(tuple(map(int, input().split())))

arr.sort(key=lambda x: x[0])  # 이분 탐색 쓸 거라서 정렬

# 최대로 전깃줄이 꼬이지 않고 최대로 들어있으려면 단조 증가(동일 위치 전깃줄 없다는 조건 있음) 수열을 만들어야 한다.

lines = []
for i in range(n):
    b = arr[i][1]
    if i == 0:  # 아무 것도 없다면 방해 없이 전깃줄을 건다.
        lines.append(b)
    else:
        if b > lines[-1]:  # 꼬이지 않는 새로운 줄이 증가한다.
            lines.append(b)
        else:
            s, e = 0, len(lines)-1
            ans = len(lines)-1
            while s <= e:
                mid = (s+e)//2
                if lines[mid] > b:  # 현재 가지고 있는 b보다 큰 수 중에 가장 작은 수를 찾아서 대체
                    ans = mid
                    e = mid-1
                else:
                    s = mid + 1
            lines[ans] = b  # 숫자의 정확성은 중요하지 않다.
            # 이전 전깃줄 번호보다 크고 이후 전깃줄 번호보다 작은 수를 만족하는지 증가하는 전깃줄의 유무가 중요한 것.

print(n-len(lines))  # 증가하는 전깃줄 번호를 만들지 못하는 전깃줄 수 만큼 무시된다.
# 즉 전체 전깃줄 수에서 번호가 증가 수열을 이루는 전깃줄의 최대 개수(len(lines))를 빼면 가로지른 수를 구할 수 있다.
