

N = int(input())
dot = [[0 for col in range(N)] for row in range(2)]

for i in range(N):
    dot[0][i], dot[1][i] = map(int, input().split())

dot[1].sort()

for i in range(N):
    for j in range(2):
        print(dot[j][i], end=' ')
    print(" ")
