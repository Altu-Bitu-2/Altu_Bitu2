import sys
input = sys.stdin.readline

test_num = int(input())
dict = dict()
for i in range(test_num):
    n = int(input())
    result = 1
    for j in range(n):
        name, type = map(str, input().split())
        if type in dict:
            dict[type] += 1;
        else:
            dict[type] = 1;

    for value in dict.values():
        result *= (value+1)
    result -= 1
    print(result)
    dict.clear()