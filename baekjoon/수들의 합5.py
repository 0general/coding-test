'''
n = int(input())

ls = [i for i in range(1, n//2+2)]
pt2 = len(ls)-1
pt1 = pt2-1
result = 1
while pt1 > -1:
    s = sum(ls[pt1:pt2+1])
    if s == n:
        result += 1
        pt2 -= 1
    elif s > n:
        pt2 -= 1
    else:
        pt1 -= 1

print(result)


#메모리 초과
'''
n = 15

pt2 = n//2 + 1
pt1 = pt2-1
result = 1
while pt1 > 0:
    s = ((pt1 + pt2)*(pt2-pt1+1))/2
    if s == n:
        result += 1
        pt2 -= 1
    elif s > n:
        pt2 -= 1
    else:
        pt1 -= 1
    if pt1 == pt2:
        pt1 -= 1

print(result)
