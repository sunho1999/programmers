
def solution(n):
    answer = 0
    bin_number = list((bin(n)[2:]))
    # print(bin_number)
    bin_num_cnt = bin_number.count('1')
    for i in range(n+1,1000001):
        check_number = list((bin(i)[2:]))
        # print(check_number)
        check_num_cnt = check_number.count('1')
        # print(check_num_cnt)
        if check_num_cnt == bin_num_cnt:
            answer = i
            break
    return answer