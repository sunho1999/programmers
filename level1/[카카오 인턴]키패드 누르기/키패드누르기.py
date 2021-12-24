import math


def solution(numbers, hand):
    left_xy = [3, 0]
    right_xy = [3, 2]
    answer = ''
    for i in numbers:
        if i == 1:
            left_xy = [0, 0]
            answer += "L"
        elif i == 4:
            left_xy = [1, 0]
            answer += "L"
        elif i == 7:
            left_xy = [2, 0]
            answer += "L"
        elif i == 3:
            right_xy = [0, 2]
            answer += "R"
        elif i == 6:
            right_xy = [1, 2]
            answer += "R"
        elif i == 9:
            right_xy = [2, 2]
            answer += "R"
        else:
            if i == 2:
                x1 = 0
                y1 = 1
                Ltest1_x, Ltest1_y = left_xy[0], left_xy[1]
                Rtest1_x, Rtest1_y = right_xy[0], right_xy[1]
                if math.ceil(math.sqrt((Ltest1_x - x1) ** 2 + (Ltest1_y - y1) ** 2)) < math.ceil(
                        math.sqrt((Rtest1_x - x1) ** 2 + (Rtest1_y - y1) ** 2)):
                    answer += "L"
                    left_xy = [0, 1]
                elif math.ceil(math.sqrt((Ltest1_x - x1) ** 2 + (Ltest1_y - y1) ** 2)) > math.ceil(
                        math.sqrt((Rtest1_x - x1) ** 2 + (Rtest1_y - y1) ** 2)):
                    answer += "R"
                    right_xy = [0, 1]
                elif math.ceil(math.sqrt((Ltest1_x - x1) ** 2 + (Ltest1_y - y1) ** 2)) == math.ceil(
                        math.sqrt((Rtest1_x - x1) ** 2 + (Rtest1_y - y1) ** 2)):
                    if hand == "right":
                        answer += "R"
                        right_xy = [0, 1]
                    else:
                        answer += "L"
                        left_xy = [0, 1]
            elif i == 5:
                x1 = 1
                y1 = 1
                Ltest1_x, Ltest1_y = left_xy[0], left_xy[1]
                Rtest1_x, Rtest1_y = right_xy[0], right_xy[1]
                if math.ceil(math.sqrt((Ltest1_x - x1) ** 2 + (Ltest1_y - y1) ** 2)) < math.ceil(
                        math.sqrt((Rtest1_x - x1) ** 2 + (Rtest1_y - y1) ** 2)):
                    answer += "L"
                    left_xy = [1, 1]
                elif math.ceil(math.sqrt((Ltest1_x - x1) ** 2 + (Ltest1_y - y1) ** 2)) > math.ceil(
                        math.sqrt((Rtest1_x - x1) ** 2 + (Rtest1_y - y1) ** 2)):
                    answer += "R"
                    right_xy = [1, 1]
                elif math.ceil(math.sqrt((Ltest1_x - x1) ** 2 + (Ltest1_y - y1) ** 2)) == math.ceil(
                        math.sqrt((Rtest1_x - x1) ** 2 + (Rtest1_y - y1) ** 2)):
                    if hand == "right":
                        answer += "R"
                        right_xy = [1, 1]
                    else:
                        answer += "L"
                        left_xy = [1, 1]
            elif i == 8:
                x1 = 2
                y1 = 1
                Ltest1_x, Ltest1_y = left_xy[0], left_xy[1]
                Rtest1_x, Rtest1_y = right_xy[0], right_xy[1]
                if math.ceil(math.sqrt((Ltest1_x - x1) ** 2 + (Ltest1_y - y1) ** 2)) < math.ceil(
                        math.sqrt((Rtest1_x - x1) ** 2 + (Rtest1_y - y1) ** 2)):
                    answer += "L"
                    left_xy = [2, 1]
                elif math.ceil(math.sqrt((Ltest1_x - x1) ** 2 + (Ltest1_y - y1) ** 2)) > math.ceil(
                        math.sqrt((Rtest1_x - x1) ** 2 + (Rtest1_y - y1) ** 2)):
                    answer += "R"
                    right_xy = [2, 1]
                else:
                    if hand == "right":
                        answer += "R"
                        right_xy = [2, 1]
                    else:
                        answer += "L"
                        left_xy = [2, 1]
            elif i == 0:
                x1 = 3
                y1 = 1
                Ltest1_x, Ltest1_y = left_xy[0], left_xy[1]
                Rtest1_x, Rtest1_y = right_xy[0], right_xy[1]
                if math.ceil(math.sqrt((Ltest1_x - x1) ** 2 + (Ltest1_y - y1) ** 2)) < math.ceil(
                        math.sqrt((Rtest1_x - x1) ** 2 + (Rtest1_y - y1) ** 2)):
                    answer += "L"
                    left_xy = [3, 1]
                elif math.ceil(math.sqrt((Ltest1_x - x1) ** 2 + (Ltest1_y - y1) ** 2)) > math.ceil(
                        math.sqrt((Rtest1_x - x1) ** 2 + (Rtest1_y - y1) ** 2)):
                    answer += "R"
                    right_xy = [3, 1]
                elif math.ceil(math.sqrt((Ltest1_x - x1) ** 2 + (Ltest1_y - y1) ** 2)) == math.ceil(
                        math.sqrt((Rtest1_x - x1) ** 2 + (Rtest1_y - y1) ** 2)):
                    if hand == "right":
                        answer += "R"
                        right_xy = [3, 1]
                    elif hand == "left":
                        answer += "L"
                        left_xy = [3, 1]

    return answer