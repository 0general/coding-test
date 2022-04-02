"""
https://www.acmicpc.net/problem/1377
"""
import sys

input = sys.stdin.readline

mx = 0
n = int(input())
arr = [(int(input()), i) for i in range(n)]

arr.sort(key=lambda x: x[0])

for i in range(n):
    x = arr[i][1]-i
    mx = max(mx, x)

print(mx+1)

# 이문제는 사실 세그먼트 트리(idx-1까지의 숫자 중에 idx번째 숫자보다 큰 숫자들의 개수)로 풀려고 했다.
# 하지만 세그먼트 트리는 메모리를 초과하게 된다하여
# 펜윅 트리나 인덱스 트리로 도전해야한다고 했지만 아직 익숙하지 못 해,
# 새로운 방법을 구했다.
# 뒤쪽에 있다가 앞으로 오는 수가 몇 번 스왑되어야 하는지 중 최대를 구하면 된다.
# 앞에 있다가 뒤로 가는 것은 위 과정에서 다 맞춰진다.
