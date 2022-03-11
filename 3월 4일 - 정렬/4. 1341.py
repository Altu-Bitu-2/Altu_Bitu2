import sys      #sys 모듈 불러오기
input = sys.stdin.readline      #입력받기 설정

n = int(input())    #기타 개수 입력받아 저장
arr = [input().rstrip() for _ in range(n)]  #시리얼번호를 기타 개수만큼 반복하여 입력받는다.
#rstrip - 인자로 전달된 문자를 string의 오른쪽에서 제거, 전달하지 않으면 공백 제거
#lstrip(왼쪽), strip(양쪽)

def sum_digit(text):
    # 문자열에 포함된 숫자를 전부 더해 반환하는 함수입니다.
    total = 0   #합계 초기화
    for c in text:  #문자열 속 문자 하나마다
        # 문자열의 메소드 .isdigit()으로 숫자인지 판단할 수 있습니다.
        if c.isdigit(): #숫자인지 아닌지 판단하고, 만약 숫자라면
            total += int(c) #그 수를 합계에 더한다.
    return total    #계산한 합계 반환

# 정렬의 우선순위에 맞춰서 람다함수를 작성합니다.
# 첫번째는 문자열의 길이, 두번째가 숫자의 합, 세번째가 사전순 입니다.
arr.sort(key=lambda x:(len(x), sum_digit(x), x))

for i in arr:   #정렬한 시리얼 번호들을 하나씩
    print(i)    #출력한다
# 혹은 print('\n'.join(arr)) 로 한줄에 처리할 수 있습니다.
# .join 메소드는 문자열을 처리할 때 유용하니 알아두세요!