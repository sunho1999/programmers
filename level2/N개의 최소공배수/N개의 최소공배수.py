import math

def solution(arr):
    def lcm(a, b):
        return a * b // math.gcd(a, b)

    num = arr[0]
    for i in arr[1:]:
        num = lcm(num, i)
    answer = num
    return answer