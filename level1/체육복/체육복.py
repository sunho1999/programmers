def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    set_lost = lost - reserve
    set_reserve = reserve - lost
    for i in set_reserve:
        up = i +1
        down = i -1
        if down in set_lost:
            set_lost.remove(down)
        elif up in set_lost:
            set_lost.remove(up)
    return n - len(set_lost)