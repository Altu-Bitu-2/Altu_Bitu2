import sys  #sys 모듈 불러오기
from collections import deque   #deque 모듈 불러오기
input = sys.stdin.readline  #입력 설정

"""
[숫자 할리갈리 게임] - 시뮬레이션 문제
- 언어별 추가시간이 없으므로, pypy3으로 제출
- 카드 덱과 그라운드의 카드를 관리하기 위해 덱 사용
1. 차례가 되면, 상단 카드를 그라운드에 놓는다.
2. 누군가의 카드 덱이 비는 즉시 게임 종료
3. 종을 치면, 상대방의 그라운드 카드를 뒤집어서 카드 더미의 밑에 넣는다.
"""
def move_cards(card, ground):   #카드 이동 함수
    # index 에러 방지 -1 제거
    ground.popleft()

    # deque.extendleft(arr): arr에 있는 값을 하나씩 빼서 왼쪽에 삽입한다.
    card.extendleft(ground) #그라운드에 있는 카드를 가져간다.
    ground.clear()  #그라운드를 비운다

    ground.append(-1) # 인덱스 방지 -1 다시 추가
    return  #종료

def play_game(cards, ground):   #게임 진행 함수
    player = 0

    ground[0].append(-1)    # index 에러 방지
    ground[1].append(-1)    # index 에러 방지

    for _ in range(m):
        ground[player].append(cards[player].pop())  #그라운드에 카드를 내려놓는다.

        if len(cards[player]) == 0: #카드가 수가 0개라면
            return 1 - player   #상대방 승리

        player = 1 - player     # 다음 플레이어

        if ground[0][-1] == 5 or ground[1][-1] == 5: #카드 숫자가 5인 순간
            hit = 0     # 도도
        elif ground[0][-1] + ground[1][-1] == 5:    #카드 숫자 합이 5인 순간
            hit = 1     # 수연
        else:   #아니면
            continue    #넘어간다

        move_cards(cards[hit], ground[1 - hit]) #카드를 가져간다
        move_cards(cards[hit], ground[hit]) #카드를 가져간다

    if len(cards[0]) > len(cards[1]):   #도도의 카드가 더 많다면
        return 0    #도도 승리
    elif len(cards[0]) < len(cards[1]): #수연의 카드가 더 많다면
        return 1    #수연 승리
    else:  #같다면
        return 2    #비김

n, m = map(int, input().split())    #카드 개수, 게임 진행 횟수 입력받아 저장

cards = [deque() for _ in range(2)]     #카드 덱 선언
ground = [deque() for _ in range(2)]    #그라운드 덱 선언
name = ["do", "su", "dosu"]     # 출력할 이름

for _ in range(n):  #카드 개수만큼 반복하여
    a, b = map(int, input().split())    #적힌 수 입력받아 저장
    cards[0].append(a)  #도도 카드 덱에 추가
    cards[1].append(b)  #수연 카드 덱에 추가

print(name[play_game(cards, ground)])   #이긴 사람의 이름 출력