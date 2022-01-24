def solution(array, commands):
    answer = []
    for i in commands:
        start, end, idx = i[0], i[1], i[2]
        list1 = []
        list1 = array[start - 1:end]
        list1.sort()
        answer.append(list1[idx - 1])

    return answer