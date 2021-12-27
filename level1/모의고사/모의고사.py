def solution(answers):
    answer = []
    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(len(answers)):
        a1 = i % 5
        a2 = i % 8
        a3 = i % 10
        if num1[a1] == answers[i]:
            count1 += 1
        if num2[a2] == answers[i]:
            count2 += 1
        if num3[a3] == answers[i]:
            count3 += 1

    max_num = max(count1, count2, count3)
    if max_num == count1:
        answer.append(1)
    if max_num == count2:
        answer.append(2)
    if max_num == count3:
        answer.append(3)

    return answer