import sys  #sys 모듈 불러오기

input = sys.stdin.readline  #입력 설정

"""
[체스판 다시 칠하기]
- 나올 수 있는 체스판의 경우: 2가지
    - (0, 0)이 검정인 경우, 흰색인 경우
    - 검정으로 시작하는 체스판의 경우, 인덱스 i+j가 짝수일 때 'B'임을 이용

1.  (0, 0) 인덱스부터 차례로 8*8 체스판 만들 때 바꿔야 하는 칸 수를 계산하고, 그 중 최솟값 구하기

보드 크기 <= 2,500
한 위치에 대한 체스판 비교 연산 = 64번
총 연산 수 = 2,500 * 64 < 1억 -> 브루트 포스 가능
"""
SIZE = 64   #체스판 사이즈 선언


# (x, y)에서 시작하는 8*8 체스판을 만드는데 필요한 최소 카운트 리턴
# 검정으로 시작하는 체스판을 기준으로 계산(b_count) -> 절반(32) 이상이면 흰색으로 시작하는 체스판 카운트(64 - b_count) 리턴
def count_change(x, y, board):  #바꿔야 하는 횟수를 반환하는 함수
    b_count = 0 #결과값 초기화

    for i in range(8):  #행만큼 반복하여
        for j in range(8):  #열만큼 반복하여
            # 검정으로 시작하는 경우, i+j가 짝수일 때 검정, 아니면 흰색
            if (i + j) % 2 == 0 and board[x + i][y + j] != 'B': #i+j가 짝수일 때 검정이면
                b_count += 1    #결과값 1 증가
            elif (i + j) % 2 == 1 and board[x + i][y + j] != 'W': #i+j가 홀수일 때 흰색이면
                b_count += 1    #결과값 1 증가

    # 최솟값 리턴
    if b_count > SIZE // 2: #만약 결과값이 크기보다 크다면
        return SIZE - b_count  # 흰색 시작 체스판 카운트
    return b_count  # 검정색 시작 체스판 카운트


n, m = map(int, input().split())    #체스판 크기를 입력받아 저장
board = [input().rstrip() for _ in range(n)]    #체스판의 값 입력받아 저장
answer = SIZE  # 최대값으로 초기화

for i in range(n - 8 + 1):  #각 행과
    for j in range(m - 8 + 1):  #각 열에 대하여
        answer = min(answer, count_change(i, j, board))   #함수 결과값이 최소인 경우를 저장

print(answer)   #결과값 출력