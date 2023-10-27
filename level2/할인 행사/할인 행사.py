def solution(want, number, discount):
    want_list = {}
    answer = 0
    for i in range(len(number)):
        for j in range(number[i]):
            want_list[want[i]] = number[i]
    # print(want_list)
    cnt = 0
    len_discount = len(discount)
    while cnt + 10 <= len_discount:
        check_discount = discount[cnt:cnt + 10]
        # print(check_discount)

        # print(list_discount)
        for i in range(len(want)):
            check = True
            check_item = check_discount.count(want[i])
            # print(want[i])
            if want[i] not in check_discount:
                check = False
                break
            elif want_list[want[i]] < check_item or want_list[want[i]] > check_item:
                # print(want_list[list_discount[i]],check_item)
                check = False
                break
        cnt += 1
        if check == True:
            answer += 1
    # answer = cnt

    return answer