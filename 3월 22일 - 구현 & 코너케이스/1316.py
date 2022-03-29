import sys  #sys 모듈 불러오기

input = sys.stdin.readline  #입력설정

"""
[그룹 단어 체커] - 단순 구현 문제

- 이미 등장한 알파벳 저장할 set() 선언 (탐색 O(1))
- 처음 등장하는 알파벳은 set에 추가하고, 무리에서 떨어졌는데 이미 등장한 알파벳이면 그룹 단어가 아니다.

"""


def is_group_word(word):    #그룹 단어인지 판단하는 함수
    checked = set()   #이미 등장한 알파벳 저장
    prev = None     #이전의 알파벳 저장

    for c in word:  #각 알파벳마다
        if c == prev:   #연속하는 알파벳이면
            continue    #계속한다

        if c in checked:    #연속하지 않으면서 이미 등장한 알파벳이면
            return False    #그룹단어가 아니다

        checked.add(c)  #이미 등장한 알파벳으로 저장
        prev = c    #이전 알파벳이 현재 알파벳이 된다

    return True #조건을 만족하면 참이다


# 입력
n = int(input())    #단어의 개수 저장

# 입력 + 연산
count = 0   #그룹단어의 개수 저장

for _ in range(n):  #단어 개수만큼 반복하여
    word = input().rstrip()     #\n 제거하고 저장
    if is_group_word(word):     #만약 그룹단어가 맞다면
        count += 1      #그룹 단어의 수 1 증가

# 출력
print(count)    #개수 출력