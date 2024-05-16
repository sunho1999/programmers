from collections import deque


# 1번부터 n번 상자까지 번호가 증가하는 순서대로 컨테이너 벨트에 일렬로 놓여 전달
# 택배 기사님이 미리 알려준 순서에 맞게 영재가 택배 상자에 실ㅇ어야함
# 순서 아니면, 보조 컨테이너 벨트에 보관 LIFO형태


def solution(order):
    answer = 0
    number_list = [i for i in range(len(order), 0, -1)]
    # print(number_list)
    que = deque()
    idx = 0
    # print(number_list)
    while True:
        # print(que," ",idx," " ,number_list)
        if len(que) == 0:
            if len(number_list) == 0:
                break
            item = number_list.pop()  # 1
            if item != order[idx]:
                que.append(item)
            else:
                idx += 1
                answer += 1
        else:  # que에 있을 때
            que_number = que.pop()
            if len(number_list) == 0:
                if que_number != order[idx]:
                    break
            if que_number != order[idx]:  # que에 있는게 다를 때
                que.append(que_number)
                item = number_list.pop()
                if item != order[idx]:
                    que.append(item)
                elif item == order[idx]:
                    answer += 1
                    idx += 1
            else:
                answer += 1
                idx += 1

    return answer