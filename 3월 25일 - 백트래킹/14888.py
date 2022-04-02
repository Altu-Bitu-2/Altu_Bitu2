import sys  #sys 모듈 불러오기
sys.stdin.readline  #입력 설정

"""
[연산자 끼워넣기]
연산자를 모두 돌려보면서 배치한 후, 각 연산자에 따른 값 계산
"""

MAX = 10**9     #최댓값 선언

add = lambda x, y: x + y    #덧셈 정의
sub = lambda x, y: x - y    #뺄셈 정의
multiply = lambda x, y: x * y   #곱셈 정의

# C++14 방식에 맞추어 나누기 함수 작성
def division(x, y): #나눗셈 정의
    if x < 0:   #x가 음수이면
        return - (-x // y)  #양수로 바꾸어 나누고 다시 음수로 바꾼다
    return x // y   #아니면 원래대로 나눈다

# 인덱스에 맞는 연산을 하기 위해 함수를 리스트에 저장
functions = [add, sub, multiply, division]

# cnt: 수 인덱스, value: 현재까지 연산 결과
def backtracking(cnt, value):   #연산을 실행하고 결과를 저장하는 함수
    global max_value, min_value #최댓값, 최솟값을 전역변수로 선언
    if cnt == n:    # 연산이 모두 완료 되었다면
        max_value = max(max_value, value)   #최댓값 계산
        min_value = min(min_value, value)   #최솟값 계산
        return  #종료

    for i in range(4):  #연산자 종류만큼 반복하여
        if operator[i] > 0: #연산이 있다면
            operator[i] -= 1    #연산 개수를 1 감소
            backtracking(cnt + 1, functions[i](value, numbers[cnt]))    # i번째 함수에 value와 numbers[cnt]를 인자로 넘겨주어 계산함
            operator[i] += 1    #연산 개수를 1 증가
    return  #종료

# 입력
n = int(input())    #수의 개수 저장
numbers = list(map(int, input().split()))   #각 숫자 입력받아 저장
operator = list(map(int, input().split()))  #연산의 개수 입력받아 저장

max_value = -MAX   # 현재까지 최대값 기록
min_value = MAX    # 현재까지 최솟값 기록

# 연산
backtracking(1, numbers[0]) #연산 함수 실행
# 출력
print(max_value, min_value, sep='\n')   #결과의 최댓값, 최솟값 출력