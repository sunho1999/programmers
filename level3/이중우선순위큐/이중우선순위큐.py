from collections import deque

def solution(operations):
    que = deque()
    lis1 = []
    answer = []
    for i in operations:
        if i[0] == "I":
            lis1.append(int(i[2:]))
            lis1.sort()
        elif i[0] == "D":
            if len(lis1) == 0:
                pass
            elif i[2] == "-":
                del lis1[0]
            else:
                del lis1[-1]
    if len(lis1) == 0:
        answer = [0,0]
    else:
        answer.append(max(lis1))
        answer.append(min(lis1))
    return answer