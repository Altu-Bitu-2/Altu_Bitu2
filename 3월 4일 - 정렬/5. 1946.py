from operator import itemgetter

T = int(input())

for i in range(T):
    N = int(input())
    rank = [[0 for col in range(2)] for row in range(N)]
    for j in range(N):
        rank[j][0], rank[j][1] = map(int, input().split())
    max_num = N
    rank.sort(key=itemgetter(0))
    rank.sort(key=itemgetter(1))