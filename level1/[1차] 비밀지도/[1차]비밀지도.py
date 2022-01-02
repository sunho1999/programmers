def solution(n, arr1, arr2):
    list1 = [[0]*(n) for _ in range(n)]
    answer = []
    tag_arr1 = []
    tag_arr2 = []
    for i in arr1:
        tag_arr1.append(list(bin(i)[2:].zfill(n)))
    for i in arr2:
        tag_arr2.append(list(bin(i)[2:].zfill(n)))
    for i in range(n):
        for j in range(n):
            if tag_arr1[i][j] == "1" or tag_arr2[i][j] == "1":
                list1[i][j] = "#"
            else:
                list1[i][j] = " "
    for i in list1:
        answer.append("".join(i))
    print(answer)
    return answer