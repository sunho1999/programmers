from collections import defaultdict


def solution(fees, records):
    answer = []
    info_dict = defaultdict()
    use_info = defaultdict(list)
    for i in records:
        info = i.split(" ")
        time = info[0]
        hour, minn = time.split(":")
        car_name = info[1]
        state = info[2]
        if state == "IN":
            info_dict[car_name] = int(hour) * 60 + int(minn)
            # print(info_dict)
        elif state == "OUT":
            gap = (int(hour) * 60 + int(minn)) - info_dict[car_name]
            use_info[car_name].append(gap)
            del info_dict[car_name]

    if info_dict:
        for j in info_dict:
            end_time = 23 * 60 + 59
            gapp = end_time - info_dict[j]
            use_info[j].append(gapp)

    for i in use_info:
        use_info[i] = sum(use_info[i])

    for i in use_info:
        if use_info[i] > fees[0]:
            if (use_info[i] - int(fees[0])) % int(fees[2]) == 0:
                diff = int(fees[1]) + (use_info[i] - int(fees[0])) // int(fees[2]) * int(fees[3])
            else:
                diff = int(fees[1]) + ((use_info[i] - int(fees[0])) // int(fees[2]) + 1) * int(fees[3])
            answer.append((i, diff))
        else:
            answer.append((i, fees[1]))
    real_answer = sorted(answer, key=lambda x: x[0])
    # print(real_answer)
    cc = []
    for i, j in real_answer:
        cc.append(j)
    return cc