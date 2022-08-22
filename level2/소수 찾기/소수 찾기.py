from itertools import permutations
import math


# 소수 판별
def prime(x):
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:  # 나눠떨어지는 숫자가 있으면 소수가 아님
            return False
    return True  # 전부 나눠떨어지지 않는다면 소수임


def solution(numbers):
    answer = 0
    numbers = list(numbers)
    num_list = []
    len_num = len(numbers)
    comb = []
    for i in range(1, len_num + 1):
        a = list(permutations(numbers, i))
        comb += a
    for i in comb:
        te = ""
        for j in i:
            te += j
        num_list.append(int(te))
    num_list = set(num_list)
    num_list = list(num_list)
    if 1 in num_list:
        num_list.remove(1)
    if 0 in num_list:
        num_list.remove(0)
    for i in num_list:
        a = prime(i)
        if a == True:
            answer += 1
    return answer