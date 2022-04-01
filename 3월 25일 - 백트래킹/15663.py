import sys  #sys 모듈 불러오기

input = sys.stdin.readline  #입력 설정

"""
 1. 우선 수열을 사전 순으로 증가하는 순서로 출력해야 하므로 주어진 수열을 오름차순 정렬
 2. 이 상태에서 우선, 같은 위치의 수를 또 선택하지 않도록 중복제거 (check 배열 사용)를 해줌
 3. 그 후, 중복되는 "수열"을 거르는 방법은 이전에 선택한 값을 변수에 저장해서, 수열을 만들다 다시 루트 노드로 돌아왔을 때
    이전에 선택한 값과 같은 값이면 넘어가면 됨! -> 어차피 같은 수이므로 같은 과정 반복해서 똑같은 수열이 나올 것
"""


def backtracking(idx, m):   #조건을 만족하는 수열을 찾아 출력하는 함수
    if idx == m:    #다 선택했다면
        print(*answer)  # *list -> 리스트의 요소를 하나씩 풀어서 print()에 인자로 넣어줌
        # print(*[1, 2, 3]) == print(1, 2, 3)
        return  #종료

    prev = 0  # 이전에 선택한 값
    for i in range(n):  #숫자 개수만큼 반복
        if not checked[i] and arr[i] != prev:   #이전에 선택한 위치와 값이 아니면
            checked[i] = True   #선택 상태 저장
            prev = arr[i]   #이전에 선택한 값에 현재 값 저장
            answer[idx] = arr[i]    #정답 수열에 추가
            backtracking(idx + 1, m)    #이후의 수열을 계산
            checked[i] = False  #선택하지 않은 상태 저장

    return  #종료


n, m = map(int, input().split())    #n, m 입력받아 저장
arr = list(map(int, input().split()))   #숫자 저장
arr.sort()  #숫자를 오름차순 정렬
checked = [False] * n   #중복 제거용 배열 초기화
answer = [0] * m    #정답 배열 초기화

backtracking(0, m)  #수열 함수 실행