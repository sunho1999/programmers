def solution(s):


    def bin_change(s, zero_cnt, change_cnt):
        new_word = ""
        # print(s)
        if s == "1":
            return [change_cnt, zero_cnt]
        else:
            for i in s:
                if i == "1":
                    new_word += i
                elif i == "0":
                    zero_cnt += 1
            new_word = len(new_word)
            new_word = bin(new_word)[2:]
            change_cnt += 1
            new_word = str(new_word)
            return bin_change(new_word, zero_cnt, change_cnt)

    answer = bin_change(s, 0, 0)
    return answer
