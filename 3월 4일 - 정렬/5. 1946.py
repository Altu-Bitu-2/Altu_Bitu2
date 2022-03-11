import sys  #sys 모듈 불러오기
input = sys.stdin.readline  #입력받기 설정

def solve(n, arr):  #최대 인원수를 반환하는 함수 정의
    arr.sort()
    # key 값이 따로 없이 정렬했으므로, 서류 점수의 오름차순, 그 이후 면접 순위의 오름차순으로 정렬이 되어있다.
    # 따라서 앞에서 부터 탐색하면서 면접 순위에 대한 조건을 만족하는지 확인해야 한다.
    count = 0   #최대 인원수 초기화
    best_rank = n   # 현재까지 면접 순위 중 가장 높은 순위를 기록한다.
    for rank in arr:    #전체 순위 중 각 지원자의 순위가
        # 이미 서류 점수의 오름차순으로 정렬했으므로, 현재 최고의 면접 순위보다 우수해야 선발할 수 있다.
        if rank[1] < best_rank: #현재의 가장 높은 면접순위보다 더 높다면
            count += 1  #최대 인원수에 1명 추가
            best_rank = rank[1] #가장 높은 면접 순위를 현재 지원자의 면접 순위로

    return count    #최대 인원수 반환


T = int(input())    #테스트 케이스의 개수 입력받기
for _ in range(T):  #테스트 케이스 개수만큼 반복하여
    n = int(input())    #지원자의 수 입력받기
    arr = [list(map(int, input().split())) for _ in range(n)]   #서류심사 성적, 면접 성적 순위 입력받아 저장
    print(solve(n, arr))    #함수를 호출하고 결과 출력