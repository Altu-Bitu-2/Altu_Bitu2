import sys
input = sys.stdin.readline

n, m = map(int, input().split(":"))

def gcdIter(a, b):
  while(b):
    a = a % b
    a,b = b,a
  return a

if n==m:
  n=m=1
elif n>m:
  gcd = gcdIter(n,m)
else:
  gcd = gcdIter(m,n)
n = n // gcd
m = m // gcd

print("%d:%d" %(n, m))