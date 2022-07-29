
def solution(dirs):
    answer = 0
    point_list = []
    center_x = 5
    center_y = 5

    for i in dirs:
        if i == "U":
            if 0<= center_x  <= 10 and 0<= center_y-1 <= 10:
                point_list.append((center_x,center_y,center_x,center_y-1)) # 출발 x,y좌표 도착 x,y좌표식으로 저장
                point_list.append((center_x,center_y-1,center_x,center_y)) # 도착 x,y좌표 출발 x,y좌표식으로 저장
                # 2개씩 추가하는 이유는 LRL일때 왕복을 제거하기위해서
                center_y = center_y -1
            else:
                center_x = center_x
                center_y = center_y
        elif i == "D":
            if 0<= center_x <= 10 and 0<= center_y+1 <= 10:
                point_list.append((center_x,center_y,center_x,center_y+1))
                point_list.append((center_x,center_y+1,center_x,center_y))
                center_y = center_y +1
            else:
                center_x = center_x
                center_y = center_y
        elif i == "R":
            if 0<= center_x+1 <= 10 and 0<= center_y <= 10:
                point_list.append((center_x,center_y,center_x+1,center_y))
                point_list.append((center_x+1,center_y,center_x,center_y))
                center_x = center_x +1
            else:
                center_x = center_x
                center_y = center_y
        elif i == "L":
            if 0<= center_x-1 <= 10 and 0<= center_y <= 10:
                point_list.append((center_x,center_y,center_x-1,center_y))
                point_list.append((center_x-1,center_y,center_x,center_y))
                center_x = center_x -1
            else:
                center_x = center_x
                center_y = center_y

    point_list = set(point_list)
    answer = len(point_list)//2
    return answer


