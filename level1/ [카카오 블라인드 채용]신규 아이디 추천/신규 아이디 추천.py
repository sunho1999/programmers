def solution(new_id):
    answer = ''
    new_id = new_id.lower()  # 1단계
    test_2 = ''
    alpha = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "=", "+", "[", "{", "]", "}", ":", "?", ",", "<",
             ",", ">", "/"]
    for i in new_id:  # 2단계
        if i in alpha:
            pass
        else:
            test_2 = test_2 + i
    new_id = test_2
    cnt = 0
    test_3 = ""
    for i in new_id:
        if i == ".":
            if cnt < 1:  # .이 1개까지 있을 때
                test_3 = test_3 + i
                cnt += 1
        else:
            test_3 = test_3 + i

            cnt = 0
    new_id = test_3
    if len(new_id) == 1:
        if new_id[0] == ".":  # 4단계
            new_id = ""
    else:
        if new_id[0] == ".":  # 4단계
            new_id = new_id[1:]
        if new_id[-1] == ".":
            new_id = new_id[:-1]

    if new_id == "":  # 5단계
        new_id = new_id + "a"

    if len(new_id) >= 16:  # 6단계
        new_id = new_id[0:15]

        if new_id[-1] == ".":
            new_id = new_id[:-1]

    if len(new_id) <= 2:  # 7단계
        while (len(new_id) != 3):
            new_id = new_id + new_id[-1]

    answer = new_id
    return answer