import sys  #sys 모듈 불러오기

input = sys.stdin.readline  #입력 설정

"""
[골드바흐의 추측]
1. 에라토스테네스의 체를 활용하여 최댓값까지의 소수를 미리 탐색한다.
2. 가능한 소수의 차이가 커야 하므로, 작은 수부터 탐색하다가 골드바흐의 추측을 만족하면 바로 종료한다.
"""

MAX = 1000000   #정수의 최대값 설정


def find_prime():   #소수 참 거짓 리스트를 반환하는 함수
    # 소수인지 여부를 판단해서 리스트 형태로 돌려주는 함수
    is_prime = [True] * (MAX + 1)   #리스트 초기화

    root_MAX = MAX ** (1 / 2)   #효율성을 위해 루트값까지만 확인

    for i in range(2, int(root_MAX) + 1):   #3부터 최대값의 루트값까지
        # i가 소수라면
        if is_prime[i]: #i가 소수인 경우
            for j in range(i * i, MAX, i):  #i의 배수들은
                is_prime[j] = False     #소수가 아니다

    # 소수가 아닌 것들을 표기
    # 이 문제에서는 홀수인 소수만을 취급하므로 2도 제외
    is_prime[0] = is_prime[1] = is_prime[2] = False #소수가 아닌 수 제외

    return is_prime #리스트 반환


# 소수를 찾는 과정은 한번만 한다. -> 반복문 밖에서 함수 호출
is_prime = find_prime() #전체에 쓸 소수 리스트를 미리 찾는다

while True: #0이 아닐 때까지 계속해서 반복
    n = int(input())    #n을 입력받아 저장
    if n == 0:  #입력값이 0이라면
        break   #중단

    # 3부터 n//2까지 홀수만 검사
    # n//2 + 1 이상에서의 탐색은 필요 없음.
    for i in range(3, n // 2 + 1, 2):   #3부터 n//2까지 홀수만 - 1, 2 제외하고 짝수도 제외
        # i와 n-i가 둘 다 소수이면 더해서 n이 되는 두 소수를 찾은 것이므로 종료
        if is_prime[i] and is_prime[n - i]: #더해서 n인 두 수가 전부 소수이면
            print(n, '=', i, '+', n - i)    #결과를 출력하고
            break   #종료한다
    # for-else문: for문이 break에 의해 종료되지 않고, 반복문이 끝까지 돌아 정상 종료된 경우 else문으로 들어갑니다.
    else:   #소수의 합을 찾지 못한 경우
        print("Goldbach's conjecture is wrong.")    #문장 출력하고 종료