import sys  #sys 모듈 불러오기
input = sys.stdin.readline  #입력 설정

"""
 [팰린드롬 만들기] - 단순 구현 문제.ver2
 팰린드롬 문자열은 part1(part3의 대칭) + part2(최대 1글자) + part3(part1의 대칭)으로 이루어진다.
 1. 팰린드롬 문자열을 만들기 위해, 문자열을 리스트에 담아 정렬한다.
 2. 리스트의 앞부터 part1에 문자를 더해나간다.
 3. 만약 알파벳의 개수가 홀수인 경우, part2에 할당하고, 이미 part2에 문자가 있는 경우엔 팰린드롬을 만들 수 없다.
"""

name = list(input().rstrip())   #문자열을 입력받고 \n 제거해서 리스트로 저장
name.sort() # 여러 개라면 알파벳 순서가 먼저 오는 게 출력되므로 sort 해 줌

part1 = [] # 반복되는 알파벳이 있다면 순서대로 들여보낼 list
part2 = ''  #중심에 있는 part2를 초기화

status = 0  # 팰린드롬 알파벳이 만들어졌는지 저장하는 flag 변수

n = 0   #문자열에서 문자의 순서를 저장할 변수
while (n < len(name)): # name에 있는 걸 차례차례 검사할 while문
    if n+1 < len(name) and name[n] == name[n+1]: # 뒤에 같은 문자가 온다면
        part1.append(name[n]) # 하나를 넣어 주고 다음 건 pass
        n += 1  #그 뒤의 문자로
    else:   #뒤에 다른 문자가 온다면
        if part2 == '': #part2(문자열의 중앙)이 비어있다면
            part2 = name[n] # 같은 것이 홀수 개라면 -> 홀수 개는 무조건 하나여야 함
        else:   #이미 차있다면
            status = 1  #팰린드롬을 만들 수 없다
            break   #반복문 종료
    n += 1  #다음 문자로

if status == 0: #팰린드롬 알파벳이 만들어졌다면
    print(''.join(part1) + part2 + ''.join(reversed(part1)))    #결과를 출력한다
else:   #만들어지지 않았다면
    print("I'm Sorry Hansoo") # 주의! 문자열에 '가 들어있기 때문에, ""로 감싸주어야 합니다.