def solution(d, budget):
    d.sort()
    answer = 0
    total_sum = 0
    for i in d:
        total_sum += i
        if total_sum <= budget:
            answer +=1

    return answer