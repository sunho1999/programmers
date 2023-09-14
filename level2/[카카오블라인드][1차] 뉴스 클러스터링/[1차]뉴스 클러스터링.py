def solution(str1, str2):
    answer = 0
    merge_str1 = []
    merge_str2 = []
    for i in range(1,len(str1)):
        temp = str1[i-1] + str1[i]
        if temp.isalpha() == True:
            merge_str1.append(temp.upper())
    for i in range(1,len(str2)):
        temp = str2[i-1] + str2[i]
        if temp.isalpha()==True:
            merge_str2.append(temp.upper())

    str_g = []
    for i in (set(merge_str1+merge_str2)):
        k = merge_str1.count(i)
        l = merge_str2.count(i)
        m = min(k,l)
        str_g.append(m)

    str_t = []
    for i in (set(merge_str1+merge_str2)):
        k = merge_str1.count(i)
        l = merge_str2.count(i)
        m = max(k,l)
        str_t.append(m)


    if sum(str_g) != 0 and len(str_t) != 0:
        answer = int((sum(str_g) / sum(str_t)) * 65536)
    elif sum(str_g) == 0 and len(str_t) != 0:
        return 0
    else:
        return 65536
    return answer
