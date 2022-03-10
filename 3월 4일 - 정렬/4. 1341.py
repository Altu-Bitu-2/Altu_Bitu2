import re
from functools import cmp_to_key

def sum(list):
    sum = 0
    for i in list:
        sum += int(i)
    return sum

def compare(a, b):
    if len(a) == len(b):
        a_num = re.findall("\d", a)
        b_num = re.findall("\d", b)
        if sum(a_num)<sum(b_num):
            return 1;
        elif sum(a_num)>sum(b_num):
            return -1;
        else:
            return(a<b)
            #사전
    elif len(a) < len(b):
        return 1;
    else:
        return -1;

N = int(input())
serial = [0 for i in range(N)]

for i in range(N):
    serial[i] = input()

#print(compare(serial[1], serial[3]))

sorted = sorted(serial, key=cmp_to_key(compare))
print(sorted)