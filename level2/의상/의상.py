def solution(clothes):
    answer = 1
    clothes_closet = {}
    for i in range(len(clothes)):
        cloth = clothes[i][0]
        types = clothes[i][1]
        if types not in clothes_closet:
            clothes_closet[types] = 0
            clothes_closet[types] +=1
        else:
            clothes_closet[types] +=1
    for i in clothes_closet.values():
        answer = answer * (i+1)
    answer -=1
    # 한종류에 있는 수를 n이라 뽑는 경우의수
    # (n+1) * (n1+1) * (n2+1)- 1

    return answer