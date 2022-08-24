from collections import deque

def solution(s):
    answer = True

    a_list = deque(s)
    right = deque()
    left = deque()
    right_check = 0  # 체크해야할 ) 괄호 수
    while a_list:
        a = a_list.popleft()
        if a == ")":
            right.append(a)
            if len(left) == 0:
                answer = False
            else:  # left가 있을 때
                if right_check > 0:
                    right_check -= 1

        else:  # left 만났을 때
            left.append(a)
            right_check += 1
    if right_check != 0:
        answer = False
    return answer