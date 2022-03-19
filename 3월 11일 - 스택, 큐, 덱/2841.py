import sys  #sys 모듈 불러오기
input = sys.stdin.readline  #입력 설정

"""
[외계인의 기타연주]
각 줄마다 외계인이 누르고 있는 프렛을 스택에 저장하기
매 입력에 대해 이번에 누를 프렛이 해당 줄에서 가장 높은 프렛이어야 함

1. 이번에 눌러야 할 프렛보다 높은 프렛에서 손가락을 전부 떼기
2. 만약 이번에 눌러야 할 프렛을 누르고 있지 않다면 누르기
"""

n, p = map(int, input().split())    #음의 수와 프렛의 수를 입력받아 저장
stack = [[0] for _ in range(7)]  # 1번 줄부터 6번줄 까지
# 매번 스택이 비었는지 확인할 필요 없도록 미리 0번을 스택에 넣어 둠
answer = 0  #최소 움직임을 저장할 변수

for _ in range(n):  #음의 수 만큼 반복하여
    # 입력
    line, fret = map(int, input().split())  #줄 번호와 프렛 번호 입력받아 저장

    # 연산
    while stack[line][-1] > fret:    # 프렛에서 손가락 떼기
        stack[line].pop()   #프렛 번호를 스택에서 뺀다
        answer += 1 #움직임이 한 번 늘어난다
    if stack[line][-1] != fret:    # 프렛 누르기
        stack[line].append(fret)    #프렛 번호를 스택에 넣는다
        answer += 1     #움직임이 한 번 늘어난다


print(answer)  # 출력