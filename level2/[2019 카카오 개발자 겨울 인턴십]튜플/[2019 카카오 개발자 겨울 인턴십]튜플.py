def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    # print(s)
    s.sort(key=len)

    for i in s:
        new_text = i.split(",")
        # print(new_text)
        for i in new_text:
            if int(i) not in answer:
                answer.append(int(i))
    # print(answer)
    return answer