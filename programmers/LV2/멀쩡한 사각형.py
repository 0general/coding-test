def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def solution(w, h):
    g = gcd(w, h)
    a = w//g
    b = h//g
    if a > b:
        a, b = b, a
    ystack = [0]
    square = 0
    def y(x): return int((b/a)*x)
    for i in range(1, a):
        ystack.append(y(i))
        square += (a-i)*(ystack[-1]-ystack[-2])
    square *= 2
    if g == 1:
        return square
    else:
        return w*h - ((a*b)-square)*g
