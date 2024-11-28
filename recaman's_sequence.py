## Get input
## a(0) = 0; if n = 0
## for n in 1 to MAXN:
##      a(n) = a(n-1) - n
##      if a[n] is negative or already in the sequence:
##              a[n] = a(n) = a(n-1) + n
import time

def recaman_sequence(MAXN):
	r_seq = [0] * MAXN
	r_set = {0}
	for number in range(1,MAXN):
		tmp = r_seq[number-1] - number
		if tmp < 0 or tmp in r_set:
			r_seq[number] = r_seq[number-1] + number
		else:
			r_seq[number] = tmp
		r_set.add(r_seq[number])
	print(r_seq)        
        
    
while True:
	input_num = input("input a number: ")
	number= int(input_num)
	start = time.time()
	recaman_sequence(number)
	end = time.time()
	print(end-start)
