def solution(s):
    answer = ''
    list1 = []
    for i in s:
        list1.append(i)
    print(list1)

    len1 = len(s) // 2

    if len(s) % 2 == 0:
        answer = list1[len1 - 1] + list1[len1]
    else:
        answer = list1[len1]
    return answer