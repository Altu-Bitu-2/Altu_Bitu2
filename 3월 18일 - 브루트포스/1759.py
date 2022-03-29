import sys  #sys 모듈 불러오기

sys.setrecursionlimit(10 ** 6)  #재귀 깊이 늘리기
input = sys.stdin.readline  #입력 설정

"""
[암호 만들기] - ver2. 재귀함수

재귀함수를 이용해 경우의 수를 구하는 풀이
"""


# 암호가 될 수 있는지 확인하는 함수
def is_valid(cypher):
    vowels = set("aeiou")  # 모음 저장
    count = 0  # 모음 수
    for i in cypher:    #암호의 글자마다
        if i in vowels: #만약 모음이 있다면
            count += 1  #모음 수가 1씩 증가

    # 모음 한개 이상, 자음 2개 이상
    return count >= 1 and len(cypher) - count >= 2


def make_cypher(idx, cnt, cypher):  # idx: 현재 보고 있는 알파벳의 index, cnt: 남은 알파벳의 개수, cypher: 현재까지 만들어진 암호
    if cnt == 0:  # 알파벳을 모두 선택한 경우
        if is_valid(cypher):    #만약 현재까지의 암호가 암호가 될 수 있다면
            answer.append(cypher)   #정답 리스트에 추가하고
        return  #종료한다

    if idx == len(alphabets):   #현재 알파벳의 인덱스가 마지막 인덱스라면
        return  #종료한다

    make_cypher(idx + 1, cnt - 1, cypher + alphabets[idx])  # 이번 알파벳을 포함하는 경우
    make_cypher(idx + 1, cnt, cypher)  # 이번 알파벳은 포함하지 않는 경우


# 입력
n, m = map(int, input().split())    #n,m을 입력받아 저장한다
alphabets = list(input().split())   #알파벳들을 입력받아 저장한다

alphabets.sort()  # 오름차순 암호를 만들기 위해 정렬
answer = []  # 가능한 암호를 저장하는 리스트

# 연산
make_cypher(0, n, "")   #암호문 만드는 연산을 실행한다

# 출력
for i in answer:    #결과 리스트에 저장된 값들을
    print(i)    #출력한다
