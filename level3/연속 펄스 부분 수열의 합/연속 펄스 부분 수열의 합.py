def solution(sequence):
    def start_minus(sequence):
        start_minus_list = []
        for i in range(len(sequence)):
            if i % 2 == 0:
                num1 = sequence[i] * (-1)
                start_minus_list.append(num1)
            else:
                num1 = sequence[i] * 1
                start_minus_list.append(num1)
        return start_minus_list

    def start_plus(sequence):
        start_plus_list = []
        for i in range(len(sequence)):
            if i % 2 == 0:
                num1 = sequence[i] * (1)
                start_plus_list.append(num1)
            else:
                num1 = sequence[i] * -1
                start_plus_list.append(num1)
        return start_plus_list

    plus = start_plus(sequence)
    minus = start_minus(sequence)

    def check(data):
        Table = [0 for _ in range(len(sequence))]
        Table[0] = data[0]
        myMax = -987987987
        for i in range(1, len(sequence)):
            if Table[i - 1] + data[i] > data[i]:
                Table[i] = Table[i - 1] + data[i]
            else:
                Table[i] = data[i]

        for i in range(len(sequence)):
            if Table[i] > myMax:
                myMax = Table[i]
        # print(Table)
        return myMax

    aa = check(plus)
    bb = check(minus)
    # print(aa,bb)

    answer = max(aa, bb)
    return answer