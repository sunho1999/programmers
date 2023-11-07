from collections import deque

def solution(elements):
    num_list = []
    answer = 0
    cnt = 1
    que = deque(elements)
    max_num = len(elements)

    while (cnt <= max_num):
        new_elements = elements + elements[0:cnt]
        for i in range(len(new_elements)):
            # print(elements)
            sum1 = sum(new_elements[i:i + cnt])
            num_list.append(sum1)
        # break
        cnt += 1
    num_list = set(num_list)
    numt_list = list(num_list)
    # print(num_list)
    answer = len(num_list)
    return answer