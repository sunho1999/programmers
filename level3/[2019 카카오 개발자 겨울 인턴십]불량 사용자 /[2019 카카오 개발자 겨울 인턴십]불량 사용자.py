import collections


def generate_unique_combinations_dfs(data, index, current_combination, result):
    if index == len(data):
        result.append(current_combination.copy())
        return

    for item in data[index]:
        if item not in current_combination:
            current_combination.append(item)
            generate_unique_combinations_dfs(data, index + 1, current_combination, result)
            current_combination.pop()


def generate_unique_combinations(data):
    result = []
    generate_unique_combinations_dfs(data, 0, [], result)
    return result


def solution(user_id, banned_id):
    answer = list()

    for i in range(len(banned_id)):  # ban 아이디 탐색
        check_user = [True for _ in range(len(user_id))]  # check_list
        for j in range(len(user_id)):  # user 아이디 idx 탐색
            for k in range(len(user_id[j])):  # user 탐색
                if len(banned_id[i]) == len(user_id[j]):
                    if banned_id[i][k] == user_id[j][k]:
                        pass
                    else:
                        if banned_id[i][k] == "*":
                            pass
                        else:
                            check_user[j] = False
                else:
                    check_user[j] = False
        # for i in range(len(banned_id)): # ban 아이디 탐색
        #     check_user = [True for _ in range(len(user_id))] # check_list
        #     for j in range(len(user_id[i])): # user 아이디 idx 탐색
        #         for k in range(len(user_id)): # user 탐색
        #             if len(banned_id[i]) == len(user_id[k]):
        #                 if banned_id[i][j] == user_id[k][j]:
        #                     pass
        #                 else:
        #                     if banned_id[i][j] == "*":
        #                         pass
        #                     else:
        #                         check_user[k] = False
        #             else:
        #                 check_user[k] = False
        list1 = []
        for i in range(len(check_user)):
            if check_user[i] == True:
                list1.append(user_id[i])
        answer.append(list1)

    unique_combinations = generate_unique_combinations(answer)
    answer_list_str = []
    for i in range(len(unique_combinations)):
        unique_combinations[i].sort()
        tmp_str = " ".join(unique_combinations[i])
        answer_list_str.append(tmp_str)

    # print(banned_dic)
    # print(len(collections.Counter(answer_list_str)))
    answer = len(collections.Counter(answer_list_str))
    return answer