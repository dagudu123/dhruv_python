import sys
import time
sys.set_int_max_str_digits(21000)

fib=[1,1]
start = time.time()
for i in range(1,100000):
	#print(fib[0])
	tmp=0
	for i in fib:
		tmp += i

	for i in range(0, len(fib) - 1, 1):
		fib[i] = fib[i+1]

	fib[-1] = tmp


end = time.time()
print(fib[0])
print(end - start)

