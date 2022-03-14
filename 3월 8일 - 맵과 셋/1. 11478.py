import sys
input = sys.stdin.readline

s = input()
set = set()

for i in range(len(s)):
    for j in range(len(s)):
        set.add(s[i:j])
set.remove('')

print(len(set))


