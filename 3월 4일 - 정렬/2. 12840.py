import sys      #sys 모듈 불러오기
input = sys.stdin.readline  #입력받기 설정

# 연산의 편리함을 위해, 모든 시간은 초로 바꾸어 연산합니다.
MIN = 60    #1분 = 60초 변환
HOUR = 60 * MIN     #1시간 = 60분 변환
DAY = 24 * HOUR     #1일 = 24시간 변환

h, m, s = map(int, input().split())     #현재 시간 h, m, s값 입력받아 변수에 저장
q = int(input())    #쿼리 개수값 입력받아 변수에 저장

time = h*HOUR + m*MIN + s   #총 시간을 초로 바꾸어 저장

def print_time(t):  #시간 출력 함수
    h = t // HOUR   #시간 단위 계산
    t %= HOUR   #남은 시간 계산
    m = t // MIN    #분 단위 계산
    t %= MIN    #남은 시간 계산
    s = t   #초 단위 계산

    print(h, m, s)  #결과 출력

def change_time(c):
    # 현재시간(t)에 c초를 더하는 함수

    # 전역 변수를 바꾸고 싶을 때는 global 키워드를 사용합니다.
    # 만약 사용하지 않으면? 값을 참조하는건 괜찮지만, 변수에 값을 새로 할당하게 되면 함수 내에서 지역 변수가 선언됩니다. 지역변수는 함수가 종료되면서 사라지므로, 전역변수는 바뀌지 않습니다.
    global time
    # 하루가 넘어가거나, 초가 음수가 되었을 수도 있으니 모듈러 연산을 합니다.
    # python의 %와 cpp의 %는 조금 다르게 작동하니까 유의!!
    # ex. (python3) (-4) % 10 -> 6  /  (c++) (-4) % 10 -> 4
    time = (time + c) % DAY     #변화된 시간으로 반영

for _ in range(q):  #쿼리 개수만큼 반복
    # 한 줄에 몇개의 입력이 들어올지 모르는 상황이므로 리스트로 입력을 받습니다.
    query = list(map(int, input().split()))

    if query[0] == 1:   #T가 1이면 시계를 앞으로 c초만큼 돌린다.
        change_time(query[1])
    elif query[0] == 2: #T가 2면 시계를 뒤로 c초만큼 돌린다.
        # 시계를 뒤로 돌려야 하므로, 음수로 바꾸어 함수에 전달합니다.
        change_time(-query[1])
    else:   #T가 3이면 시계의 상황을 출력한다.
        print_time(time)