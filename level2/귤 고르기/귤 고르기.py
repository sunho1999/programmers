def solution(k, tangerine):
    answer_list = []
    answer = 0
    tang = {}
    for i in tangerine:
        if i not in tang:
            tang[i] = 0
            tang[i] += 1
        else:
            tang[i] += 1
    sorted_tang = dict(sorted(tang.items(), key=lambda item: item[1], reverse=True))

    total_sum = 0
    for i in sorted_tang:
        if k <= 0:
            return answer
        k -= sorted_tang[i]
        answer += 1

    return answer