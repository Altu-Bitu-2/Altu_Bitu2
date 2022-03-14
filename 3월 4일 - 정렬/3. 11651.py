import sys      #sys 모듈 불러오기
input = sys.stdin.readline  #입력받기 설정

n = int(input())    #점의 개수 입력받기
arr = [list(map(int, input().split())) for _ in range(n)]   #점의 개수만큼 반복하여 입력받아 리스트에 저장
# 정렬의 우선순위에 맞춰 람다함수를 작성합니다.
arr.sort(key=lambda x:(x[1], x[0])) #주어진 기준에 맞춘 람다힘수로 리스트를 정렬한다.

for x, y in arr:    #리스트 속의 x, y값들을
    print(x, y)     #출력한다.