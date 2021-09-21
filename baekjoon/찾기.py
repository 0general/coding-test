'''
KMP
https://www.acmicpc.net/problem/1786
'''
'''
t = input()
p = input()

m = len(p)
next = [0]*m


def initNext(p, m):
    i = 1
    j = 0
    while i < m:
        if p[i] == p[j]:
            next[i] = j + 1
            j += 1
        else:
            j = 0
        i += 1


initNext(p, m)
i = 0  # text index
j = 0  # pattern index
loc = []


while i < len(t) and j < m:
    if t[i] == p[j]:
        i += 1
        j += 1
    else:
        if j != 0:
            j = next[j-1]
        else:
            i += 1
            j = 0
    if j >= m:
        loc.append(i+1-len(p))
        i -= 1
        j -= 1
        if j != 0:
            j = next[j-1]

print(len(loc))
for k in loc:
    print(k, end=' ')
'''
t = input()
p = input()
m = len(p)
next = [0]*m


def initNext(p, m):
    i = 1
    j = 0
    while i < m:
        while i < m and j < m and p[i] == p[j]:
            j += 1
            next[i] = j
            i += 1
        if j == 0:
            i += 1
        else:
            j = next[j-1]


initNext(p, m)
i = 0  # text index
j = 0  # pattern index
loc = []
while i < len(t):
    while i < len(t) and j < len(p) and t[i] == p[j]:
        i += 1
        j += 1
        if j == len(p):
            loc.append(i - len(p) + 1)
    if j == 0:
        i += 1
    else:
        j = next[j-1]

print(len(loc))
for k in loc:
    print(k, end=' ')
