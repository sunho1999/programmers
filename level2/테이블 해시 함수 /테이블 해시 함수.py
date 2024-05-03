def solution(data, col, row_begin, row_end):
    # print(data)
    answer = 0
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    list1 = []
    for i in range(row_begin - 1, row_end):
        sum1 = 0
        for j in data[i]:
            sum1 += j % (i + 1)
        answer ^= sum1
    # print(list1)

    return answer