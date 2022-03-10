
h,m,s = map(int, input().split())
total = h * 3600 + m * 60 + s
q = int(input())

for i in range(q):
    query = input().split()
    T = int(query[0])

    if(T==1):
        c = int(query[1])
        total += c
    elif(T==2):
        c = int(query[1])
        total -= c
    elif(T==3):
        h = total//3600
        m = (total%3600)//60
        s = total%60
        print(h,m,s)
    else:
        continue;
