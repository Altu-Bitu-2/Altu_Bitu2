import sys
input = sys.stdin.readline

n = int(input())

def drainage(num):
    num_list = list(map(int, str(num)))
    sum_list = sum(num_list)
    if sum_list%3 != 0:
        return -1
    if 0 not in num_list:
        return -1
    else:
        del num_list[num_list.index(0)]
        num_list.sort(reverse=True)
        num_list.append(0)
        answer = ''.join(map(str, num_list))
        return int(answer)
    return -1

print(drainage(n))