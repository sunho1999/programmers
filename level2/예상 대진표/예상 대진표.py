# import math
# import sys
# sys.setrecursionlimit(10 ** 9)

# def solution(n,a,b):
#     global answer
#     global z
#     answer = 0
#     middle = n/2
#     z = middle
#     while n > 1:
#         n //= 2
#         answer += 1
#     # print(answer)
#     # print(middle)
#     def bin_check(middle,a,b):
#         global answer
#         global z
#         # print(answer)
#         # print(a,b,middle)
#         if a <= middle and b <= middle: # 둘다 기준보다 작을 때
#             answer -=1
#             z = z/2
#             return bin_check(middle/2,a,b)
#         elif a > middle and b > middle: # 둘다 기준보다 클 때
#             # print(a,b,middle)

#             if abs(a-middle) ==1  and abs(a-b) == 1:
#                 answer -=1
#                 return

#             else:
#                 answer -=1
#                 z = z/2
#                 return bin_check(middle + z,a,b)
#         else:
#             return
#     bin_check(middle,a,b)

#     return answer

def solution(n, a, b):
    answer = 0
    while a != b:
        answer += 1
        # 1을 더해서 2로 나누었을 때, 자리수를 맞춰줌
        # 예) 1, 2의 경우는 2, 3으로 해서 나눴을때 몫이 1이 되도록
        a, b = (a + 1) // 2, (b + 1) // 2
    return answer