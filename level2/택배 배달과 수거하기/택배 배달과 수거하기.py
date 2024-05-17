# n개의 집에 택배 배달
# 재활용 택배 상자에 담아 배달을 다니며 빈 재활용 택배 상자들을 수거하려함
# 택배는 물류 창고 보관, i번째 집은 i만큼 떨어져있음
# 트럭에는 최대cap개 만큼 실을 수 있음
# 트럭 하나로 모든 배달과 수거를 마치고 물류창고까지 돌아올 수 있는 최소 이동거리를 구하려함

def solution(cap, n, deliveries, pickups):
    answer = 0
    reverse_deliveries = deliveries[::-1]
    reverse_pickups = pickups[::-1]
    deliver = 0
    pickup = 0
    for i in range(n):
        deliver += reverse_deliveries[i]  # 2
        pickup += reverse_pickups[i]  # 0
        while deliver > 0 or pickup > 0:
            deliver -= cap
            pickup -= cap
            answer = answer + (n - i) * 2
    return answer
