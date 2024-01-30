def solution(n, s):
    answer = []
    if s // n == 0:
        answer.append(-1)
    else:
        while (n >= 1):
            left_num = s // n
            answer.append(left_num)
            s = s - left_num
            n -= 1

    return answer