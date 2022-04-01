import sys  #sys 모듈 불러오기

input = sys.stdin.readline  #입력 설정

"""
[요요 시뮬레이션] - 단순 구현 문제
체중(weight): 일일 에너지 섭취량(energy_in) - 일일 에너지 소비량(energy_out) (일일 기초 대사량(b) + 일일 활동 대사량(a))
if |일일 에너지 섭취량(energy_in) - 일일 에너지 소비량(energy_out)| > 기초 대사량 변화 역치(T)
-> 일일 기초 대사량(b) += [(일일 에너지 섭취량(energy_in) - 일일 에너지 소비량(energy_out)) / 2]
-> !주의! 이때 일일 기초 대사량에서 더해지는 값이 Floor 함수 적용이므로 음수일 때 값처리 주의해야 함

기초 대사량(b) 변화를 고려하지 않는 경우는, b == I0이므로 한번에 계산
"""


def diet_simulation(initial_weight, I0, T, period, energy_in, a):   #다이어트 시뮬레이션 함수
    b = I0  #일일 기초대사량 초기화
    weight = initial_weight     #체중 초기화
    for _ in range(period):     #다이어트 기간만큼 반복하여
        energy_out = a + b  #에너지 소비량 계산
        weight += energy_in - energy_out    #체중 계산

        if abs(energy_in - energy_out) > T:     #에너지 섭취량과 소비량의 차이가 역치보다 크다면
            b += (energy_in - energy_out) // 2  #일일 기초대사량이 변화

    return weight, b    #계산한 체중, 일일 기초 대사량을 반환


# 입력
initial_weight, I0, T = map(int, input().split())   #다이어트 전의 체중, 일일 기초대사량, 기초대사량 변화 역치 값 저장
period, energy_in, a = map(int, input().split())    #다이어트 기간, 기간동안 일일 에너지 섭취향, 일일 활동 대사량 저장

# 연산 + 출력

# 기초 대사량 변화 고려하지 않는 경우
weight = initial_weight + (energy_in - (I0 + a)) * period   #기초대사량 변화를 고려하지 않은 체중 계산
if weight <= 0: #체중이 0 이하이면
    print("Danger Diet")    #사망
else:   #아니면
    print(weight, I0)   #예상 체중, 일일 기초 대사량 출력

# 기초 대사량 변화 고려한 경우
weight, b = diet_simulation(initial_weight, I0, T, period, energy_in, a)    #기초 대사량 변화를 고려한 체중 계산

if weight <= 0 or b <= 0:   #체중이 0 이하이거나 일일 기초 대사량이 0 이하인 경우
    print("Danger Diet")    #사망
else:   #아닌 경우
    if b < I0:  #일일 기초 대사량이 줄어든 경우
        answer = "YOYO"     #요요 현상 발생
    else:
        answer = "NO"   #요요 현상이 발생하지 않음
    print(weight, b, answer)    #예상 체중, 일일 기초 대사량, 요요 발생 여부 출력