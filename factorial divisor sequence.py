import time

MAXN=10**50
def gen_primes():
	primes = []
	primes_product = 1
	for n in range(2, 10**10):
		is_prime = True
		for i in range(2, n):
			if n % i == 0:
				is_prime = False
		if is_prime: 
			primes.append(n)
			primes_product *= n
			if primes_product > MAXN: break
	return primes

start = time.time()
primes = gen_primes()

def number_of_factors(num):
	i=0
	e=0
	factors=1
	while num != 1:
		if i >= len(primes):
			print(num)
		if num % primes[i] == 0:
			num = num//primes[i]
			e = e + 1
		else:
			i = i + 1
			factors=factors * (e+1)
			e=0
    
	return factors * (e + 1)     
        
factorial=1
print(primes)

for num in range (1,101):
	factorial = factorial*num
	factors = number_of_factors(factorial)
	print(num , factors)

end = time.time()
print(end - start)
