import sys  #sys 모듈 불러오기
from itertools import permutations  #순열 모듈 불러오기

input = sys.stdin.readline  #입력 설정

"""
 [숫자 야구]
 서로 다른 세 자리 수에서 위치 + 수 같으면 스트라이크, 위치는 다르고 수가 존재하면 볼
 n개의 질문으로 수와 스트라이크와 볼 개수가 주어질 때, 이를 모두 만족하는 서로 다른 세 자리 정답 수의 개수

 [풀이]
 들어오는 모든 질문에 대해, 영수의 답과 일치하지 숫자만 남긴다.
 끝까지 남아 있는 숫자가 가능한 답의 경우의 수가 된다.
"""


def count_strike_ball(s1, s2):  #스트라이크, 볼 수를 계산하여 반환하는 함수
    # a가 답이라고 가정하고, b에 대한 스트라이크와 볼 수를 세서 리턴한다.
    strike = 0  #스트라이크 값 초기화
    ball = 0    #볼 값 초기화
    for i in range(3):  #세자리 수의 각 자리마다
        if s2[i] == s1[i]:  # 위치와 숫자가 모두 맞으면
            strike += 1 #스트라이크값 1 증가
        elif s2[i] in s1:  # 숫자는 있지만 위치가 다르면
            ball += 1   #볼값 1 증가

    return (strike, ball)   #스트라이크값, 볼값 반환


def count_answer(questions):    #답이 될 수 있는 경우의 수를 반환하는 함수
    digits = [str(i) for i in range(1, 10)] #한 자리수 정수를 리스트로 저장
    numbers = set(permutations(digits, 3))  #세자리수 정수에서 가능한 경우의 수를 순열로 해결하여 저장

    for s1, count in questions: #질문 속의 숫자들을 반복하여 탐색
        temp = set()  # 주의! 여기서 temp.clear()를 쓰면 numbers가 가 같이 비워지게 됩니다.
        for s2 in numbers:  #세자리수 정수의 모든 경우를 탐색했을 때
            if count_strike_ball(s1, s2) == count: #만약 현재 숫자들로 계산한 스트라이크, 볼값과 받아온 값이 같으면
                temp.add(s2)    #임시 셋에 현재 숫자를 추가한다
        numbers = temp  #전체 숫자의 범위를 좁힌다

    return len(numbers) #경우의 수를 반환한다

# 입력
n = int(input())    #값을 입력받아 저장
# 세자리 수는 string, 스트라이크와 볼 수는 int형으로 tuple로 묶어서 저장
initialize_input = lambda x: (x[0], (int(x[1]), int(x[2]))) #입력받을 튜플 초기화
questions = [initialize_input(input().split()) for _ in range(n)]   #질문과 답변 입력받아 저장

# 연산 + 출력
print(count_answer(questions))  #연산 결과를 출력

