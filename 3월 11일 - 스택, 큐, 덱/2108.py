import sys  #sys 모듈 불러오기
input = sys.stdin.readline  #입력 설정


N = int(input())    #수의 개수를 입력받아 저장
sum = 0     #총합을 저장할 변수
num = [0 for i in range(N)] #숫자들을 저장할 길이 N의 리스트 초기화
mode = list()   #최빈값 리스트
frequency = 1   #빈도 초기화


for i in range(N):  #전체 수만큼 반복하여
    num[i] = int(input())   #입력받은 정수를 리스트에 저장
    sum += num[i]   #각각의 원소를 더하여 총합을 계산

sorted = sorted(num)    #리스트를 오름차순으로 정렬

for i in range(N):  #전체 수만큼 반복하여
    if num.count(num[i])>frequency: #리스트에서 현재 수의 빈도가 현재까지의 최대 빈도보다 높다면
        mode.clear()    #최빈값 리스트를 비우고
        mode.append(num[i]) #현재 수만 넣는다
        frequency = num.count(num[i])   #현재 수의 빈도가 최대 빈도가 된다
    elif num.count(num[i])==frequency:  #리스트에서 현재 수의 빈도가 현재까지의 최대 빈도와 같다면
        mode.append(num[i]) #최빈값 리스트는 그대로 두고 현재 수를 넣는다
    else:   #크거나 같지 않다면
        continue    #최빈값이 아니므로 다음으로 넘어간다

mode = list(set(mode))  #반복문에서 들어간 중복 값을 제거한다
mode.sort() #최빈값 리스트를 오름차순으로 정렬한다


print(round(sum/N)) #평균(총합을 수의 개수로 나눈 값을 소수점 이하 첫째 자리에서 반올림) 출력
print(sorted[N//2]) #중앙값(수의 리스트를 오름차순으로 정렬한 뒤 중앙의 값) 출력
if len(mode)==1:    #최빈값이 하나인 경우
    print(mode[0])  #최빈값 출력
else:   #최빈값이 여러 개인 경우
    print(mode[1])  #최빈값 중 두번째로 작은 값 출력

print(sorted[N-1]-sorted[0])    #범위(정렬한 리스트의 마지막 값-처음값) 출력