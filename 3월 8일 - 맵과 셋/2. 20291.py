import sys
input = sys.stdin.readline

n = int(input())
dict = dict()

for i in range(n):
    filename, extension = map(str, input().split('.'))
    extension = extension.strip()
    if extension in dict:
        dict[extension] += 1;
    else:
        dict[extension] = 1;

result = sorted(dict.items())
for key, value in result:
    print(key, value)


