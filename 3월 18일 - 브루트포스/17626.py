import sys #sys 모듈 불러오기
from itertools import combinations_with_replacement  # 중복선택이 가능한 조합

input = sys.stdin.readline  #입력 설정

"""
[Four Squares]
자연수 n에 대해 최소 몇개의 제곱수의 합으로 표현할 수 있는지 찾는 문제
미리 최댓값까지의 제곱수를 구해놓고, 완전탐색

1. 답이 1인 경우, n이 제곱수인지만 확인해서 찾을 수 있다.
2. 2개와 3개 조합으로 불가능한 경우, 답은 무조건 4가 된다 -> 4개의 합은 시도해보지 않아도 된다.

sqrt(50000) = 약 223
전체 연산 수  < 223^2 + 223^3 = 11139296 <1억 -> 브루트포스 가능
"""

MAX = 50000     #n의 최댓값 선언


def find_min_number(n): #합이 n인 제곱수들의 최소 개수를 찾아 반환하는 함수
    squares = [i * i for i in range(1, int(MAX ** (1 / 2)) + 1)]    #제곱수를 저장한 리스트 선언

    # 만약 n이 제곱수라면
    if (int(n ** (1 / 2))) ** 2 == n:   #n이 제곱수인 경우
        return 1    #1 반환

    # 2, 3
    for num in range(2, 4): #두 제곱수나 세 제곱수를 합치는 경우
        # combinations_with_replacement() -> 중복조합
        combi = combinations_with_replacement(squares, num) #가능한 중복조합 구하기
        sum_list = list(map(lambda x: sum(x), combi))  # 모든 조합의 합 구하기
        if n in sum_list:   #n이 조합의 합과 같은 경우가 있다면
            return num  #구한 최소 개수 반환

    # 1,2,3이 아니라면
    return 4    #4 반환


# 입력
n = int(input())    #n을 입력받아 저장
# 연산 + 출력
print(find_min_number(n))   #함수를 실행하고 결과값을 출력한다