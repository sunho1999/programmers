def solution(s):
    answer = ""

    list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    text = ""
    for i in s:
        if i in num:
            answer += i
        else:
            text += i
            if text in list:
                idx = list.index(text)
                answer += num[idx]
                text = ""
    answer = int(answer)
    return answer