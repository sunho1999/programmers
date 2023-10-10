from collections import deque


def solution(s):
    s = deque(s)
    answer = 0

    def galho_check(s):
        left_big_galho = deque()
        left_middle_galho = deque()
        left_small_galho = deque()
        check = True
        for i in range(len(s)):
            if s[i] == "[":  # 대
                left_big_galho.append(s[i])
                check = True
            elif s[i] == "{":  # 중
                left_middle_galho.append(s[i])
                check = True
            elif s[i] == "(":  # 소
                left_small_galho.append(s[i])
                check = True

            elif s[i] == "]":
                if len(left_big_galho) == 0:
                    check = False
                else:
                    if (s[i - 1] == "{" and len(left_middle_galho) != 0) or s[i - 1] == "(" and len(
                            left_middle_galho) != 0:
                        check = False
                    else:
                        left_big_galho.pop()
            elif s[i] == "}":
                if len(left_middle_galho) == 0:
                    check = False
                else:
                    if (s[i - 1] == "[" and len(left_big_galho) != 0) or s[i - 1] == "(" and len(
                            left_middle_galho) != 0:
                        check = False
                    else:
                        check = True
                        left_middle_galho.pop()
            elif s[i] == ")":
                if len(left_small_galho) == 0:
                    check = False
                else:
                    if (s[i - 1] == "{" and len(left_middle_galho) != 0) or s[i - 1] == "[" and len(
                            left_big_galho) != 0:
                        check = False
                    else:
                        check = True
                        left_small_galho.pop()

        if len(left_big_galho) != 0 or len(left_middle_galho) != 0 or len(left_small_galho) != 0:
            check = False
        if check == True:
            # print(s)
            return True
        else:
            return False

    aa = galho_check(s)
    if aa == True:
        answer += 1
    for i in range(len(s) - 1):
        a = s.popleft()
        s.append(a)
        bb = galho_check(s)
        if bb == True:
            answer += 1

    return answer