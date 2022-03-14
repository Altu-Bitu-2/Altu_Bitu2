
card = [(i+1) for i in range(20)]
interval = [[0 for col in range(2)] for row in range(10)]

#역순으로 바꾸는 함수
def reverseCard(n):
    x = int(interval[n][0])
    y = int(interval[n][1])
    rvcd = card[x-1:y]
    rvcd.reverse()
    card[x-1:y] = rvcd


for i in range(10): #입력받기
    interval[i] = input().split()

for i in range(10): #카드 바꾸기
    reverseCard(i)
for i in range(20): #출력
    print(card[i], end=' ')
