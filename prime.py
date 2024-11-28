import sys
import time

primes = [2]

n=3
range = 2
count = 999
start = time.time()
while count > 0:
	#Efficient way to compute range instead of sqrt
	if range * range > n:
		range += 1
		
	prime = True
	for divisor in primes:
		if n > range:
			break
		if n % divisor == 0:
			prime = False
			break

	if (prime):
		primes.append(n)
		count -= 1
        
	n += 1
end = time.time()
print (primes)
print(end-start)
