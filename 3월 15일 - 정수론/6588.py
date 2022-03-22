import sys
input = sys.stdin.readline

def sum_prime(n, primes):
    for i in range(len(primes)):
        if (n - primes[i]) in primes:
            print("%d = %d + %d" % (n, primes[i], n - primes[i]))
            return 0
    print("Goldbach's conjecture is wrong.")
    return 0

num_list = list()
while (True):
    n = int(input())
    if n == 0:
        break;
    else:
        num_list.append(n)

m = max(num_list)
prime_tf = [True for _ in range(m+1)]
prime_tf[0] = prime_tf[1] = False
primes = []

for i in range(2, m+1):
    if prime_tf[i]:
        primes.append(i)
        for j in range(i*i, m+1, i):
            prime_tf[j] = False
for num in num_list:
    sum_prime(num, primes)