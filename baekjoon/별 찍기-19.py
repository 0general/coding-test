"""
https://www.acmicpc.net/problem/10994
"""
n = int(input())
x = (4*(n-1))+1
arr = [['*' for _ in range(x)] for _ in range(x)]


def right(x, y, length):
    for _ in range(length):
        arr[x][y] = ' '
        y += 1


def down(x, y, length):
    for _ in range(length):
        arr[x][y] = ' '
        x += 1


length = x - 2
for i in range(1, (n-1)*2+1, 2):
    right(i, i, length)
    down(i, i, length)
    right(i+length-1, i, length)
    down(i, i+length-1, length)
    length -= 4

for i in range(x):
    print("".join(arr[i]))
