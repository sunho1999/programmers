# routes배열을 진출순서대로 오름차순으로 정렬한다.
# 현재 카메라 설치위치를 나타내는 변수를 선언하고 값은 -30001로 설정한다.
# routes값을 for문으로 하나씩 탐색한다.
# 만약 진입구간이 현재 카메라의 설치구간보다 작으면, 그냥 다음 값으로 넘어간다.
# 아니라면, answer에 1을 더하고, 현재 카메라의 위치를 현재 종점위치로 갱신한다
def solution(routes):
    answer = 0
    sorted_list = sorted(routes, key=lambda x: x[0])
    check_num = -30001
    print(sorted_list)
    for i in range(len(sorted_list)):
        print(sorted_list[i][0])
        if sorted_list[i][0] > check_num:  # 다음 인덱스가 check_num보다 클 때
            print("1", sorted_list[i][0], check_num)
            check_num = sorted_list[i][1]
            answer += 1
        elif sorted_list[i][0] <= check_num:
            if sorted_list[i][1] < check_num:
                check_num = sorted_list[i][1]
            else:
                # print("2",sorted_list[i][0], check_num)
                continue

    return answer