answer = 0
answer_list = []


def prime_check(num):
    for x in range(2, num):
        if num % x == 0:
            return
    answer_list.append(num)


def solution(nums):
    sum_list = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                total_sum = nums[i] + nums[j] + nums[k]
                sum_list.append(total_sum)
    for s in sum_list:
        prime_check(s)
    answer = len(answer_list)
    return answer