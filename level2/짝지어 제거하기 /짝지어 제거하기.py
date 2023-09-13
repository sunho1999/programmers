from collections import deque


def solution(s):
    answer = 0

    len_s = len(s)
    real_que = deque(s)
    check_que = deque()
    real = real_que.popleft()
    check_que.append(real)

    for i in range(len_s - 1):
        if len(check_que) != 0:
            # print(real_que,check_que)
            real = real_que.popleft()
            check = check_que.pop()
            # print(real_que,check_que)
            if real != check:
                check_que.append(check)
                check_que.append(real)
            elif real == check:
                pass
        else:
            real = real_que.popleft()
            check_que.append(real)

    if len(check_que) == 0:
        answer = 1
    else:
        answer = 0
    return answer