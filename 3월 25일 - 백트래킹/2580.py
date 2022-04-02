import sys  #sys 모듈 불러오기

input = sys.stdin.readline  #입력 설정

"""
 가지치기 효율: 80ms

 9X9의 스도쿠에서 각 행, 열, 3x3 사각형에 1~9가 존재하는지 체크하는 2차원 배열 활용
 각 2차원 배열의 행: 어느 부분에 대한 체크인지(행, 열, 3x3), 0번 인덱스부터 시작
 각 2차원 배열의 열: 1 ~ 9 숫자 체크

 행과 열은 바로 사용하면 됨
 (ex) check_row[3][2] = true;  //3행에 2라는 숫자가 존재한다는 것
      check_col[8][9] = false; //8열에 9라는 숫자가 존재하지 않는다는 것

 3x3 사각형 (하나를 각 구역이라고 표현)
 -> 행을 3으로 나눈 몫과 열을 3으로 나눈 몫으로 구역 0부터 8까지 다음과 같이 나타낼 수 있음
 (0,0) (0,1) (0,2)
 (1,0) (1,1) (1,2)
 (2,0) (2,1) (2,2)
 -> 1차원 배열 인덱스로 구분하기 위해 각 (행 / 3)값에 3을 곱한 후 (열 / 3)을 더함
 -> 따라서 3x3 사각형의 구간은 (row / 3) * 3 + (col / 3) = 0 ~ 8인 구간으로 나눌 수 있음
"""

SIZE = 9  # 스도쿠 한 행 사이즈
check_row = [[False] * (SIZE + 1) for _ in range(SIZE)]  # 각 행의 숫자 존재 여부 체크
check_col = [[False] * (SIZE + 1) for _ in range(SIZE)]  # 각 열의 숫자 존재 여부 체크
check_3x3 = [[False] * (SIZE + 1) for _ in range(SIZE)]  # 각 3x3 사각형의 숫자 존재 여부 체크


def calc_area(x, y):    #사각형의 구간 계산
    return (x // 3) * 3 + y // 3    #계산한 값 반환


def fill_sudoku(cnt):   #스도쿠판에 숫자를 채우는 함수
    if cnt == SIZE * SIZE:  #전부 다 채웠다면
        return True #true 반환

    x, y = cnt // SIZE, cnt % SIZE  #x, y값 계산

    if sudoku[x][y] > 0:  # 이미 숫자가 채워진 칸이라면 다음 칸으로 넘어감
        return fill_sudoku(cnt + 1) #나머지 스도쿠판 채우기

    for i in range(1, SIZE + 1):  # 1~9까지 넣어보기
        if check_row[x][i] or check_col[y][i] or check_3x3[calc_area(x, y)][i]: #현재 열, 현재 행, 현재 사각형에 이미 있다면
            continue    #넘어간다

        check_row[x][i] = True  #현재 열에 있고
        check_col[y][i] = True  #현재 행에 있고
        check_3x3[calc_area(x, y)][i] = True    #현재 사각형에 있다
        sudoku[x][y] = i    #스도쿠판에 숫자를 저장

        if fill_sudoku(cnt + 1):  # 생각해보기 : 이 부분이 없으면 어떻게 될까요?
            return True     #맞는 숫자를 채웠다면 종료

        check_row[x][i] = False     #현재 열에서 제거
        check_col[y][i] = False     #현재 행에서 제거
        check_3x3[calc_area(x, y)][i] = False   #현재 사각형에서 제거
        sudoku[x][y] = 0    #스도쿠판에서 숫자 제거

    return False


# 입력
sudoku = [list(map(int, input().split())) for _ in range(SIZE)]     #스도쿠판의 숫자를 입력받아 저장

# 스도쿠 상태 표시
for i in range(SIZE):    #스도쿠판의 행 만큼 반복
    for j in range(SIZE):   #스도쿠판의 열 만큼 반복
        if sudoku[i][j] == 0:   #현재 위치의 숫자가 비어있다면
            continue    #넘어간다
        check_row[i][sudoku[i][j]] = True   #현재 열의 상태 설정
        check_col[j][sudoku[i][j]] = True   #현재 행의 상태 설정
        check_3x3[calc_area(i, j)][sudoku[i][j]] = True #현재 사각형의 상태 설정

# 연산
fill_sudoku(0)  #비어있는 숫자 채우기

# 출력
for line in sudoku: #스도쿠판의 각 행마다
    print(*line)  # *list -> 리스트의 요소를 하나씩 풀어서 print()에 인자로 넣어줌
    # print(*[1, 2, 3]) == print(1, 2, 3)