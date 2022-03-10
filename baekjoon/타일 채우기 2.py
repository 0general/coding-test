"""
https://www.acmicpc.net/problem/13976
"""
# 시간 초과
n = int(input())
mod = 1000000007

# f(x) 를 x번째에서 타일이 빠짐없이 채워지는 경우라고 계산하면
# f(x) = f(x-2)*3 + (x-2에서 한 칸만 채워지는 경우) 라고 할 수 있다.
# 이 한 칸만 채워지는 경우를 또 따져보면 f(x-4)에서 2x1 칸을 위아래로 붙이는 두가지 경우에,
# 다시 x-4에서 한 칸만 채워지는 경우를 더한 것이 된다.
# 즉 f(x) = f(x-2)*3 + 2*f(x-4) + x-4에서 한 칸만 채워지는 경우
# 정리하면 f(x) = 3*f(x-2) + 2{f(x-4) + f(x-6) + f(x-8)+ ... + f(0)} + 0(0에서 한 칸 채워지는 경우)
# f(x-2) = 3*f(x-4) + 2{f(x-6) + f(x-8) + ... + f(0)} 이므로
# f(x)-f(x-2) = 3*f(x-2) - f(x-4) 가 된다.
# 따라서 f(x) = 4*f(x-2) - f(x-4)이다.
# f(0) = 1, f(2) = 3, 홀수는 불가능
# 행렬곱을 사용하자


def matmul(num):
    if num == 1:
        return [4, -1, 1, 0]
    else:
        M = num//2
        arr = matmul(M)
        temp = [0, 0, 0, 0]
        temp[0] = (arr[0]*arr[0] + arr[1]*arr[2] + mod) % mod
        temp[1] = ((arr[0]+arr[3])*arr[1] + mod) % mod
        temp[2] = ((arr[0]+arr[3])*arr[2] + mod) % mod
        temp[3] = (arr[1]*arr[2] + arr[3]*arr[3] + mod) % mod

        if num % 2:
            arr[0] = (4*temp[0] + temp[1] + mod) % mod
            arr[1] = -temp[0]
            arr[2] = (4*temp[2] + temp[3] + mod) % mod
            arr[3] = -temp[2]
            return arr
        return temp


if n % 2:
    print(0)
elif n == 2:
    print(3)
else:
    mat = matmul(n//2-1)
    print((mat[0]*3 + mat[1]+mod) % mod)
