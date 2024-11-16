import sys
import time
from math import sqrt

MAXN=10**5000
def gen_primes():
	primes = []
	primes_product = 1
	for n in range(2, 10**10):
		is_prime = True
		for i in range(2, int(sqrt(n))+1):
			if n % i == 0:
				is_prime = False
		if is_prime: 
			primes.append(n)
			primes_product *= n
			if primes_product > MAXN: break
	return primes
start = time.time()
primes = gen_primes()

def number_of_factors(num, exponents):
	i=0
	e=0
	while num != 1:
		if i >= len(primes):
			print(num)
		if num % primes[i] == 0:
			num = num//primes[i]
			exponents[i] = exponents[i] + 1
		else:
			i = i + 1            
			e=0

	factors=1
	for e in exponents:
		if e == 0:
			break
		factors = factors*(e+1)
		

	return factors
#print(primes)
exponents=[0] * len(primes)

for num in range (1,10001):
	factors = number_of_factors(num, exponents)
	#print(factors)
end = time.time()
print(end-start)
