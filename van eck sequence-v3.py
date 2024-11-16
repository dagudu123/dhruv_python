import time
def van_eck_sequence(number):
	van_eck_seq = [0]
	steps = {}
	last_index = {0:0}
	for n in range(1,number):
		# Find the index of the previous occurence of (n-1)th term
		last_term = van_eck_seq[n-1]
		if last_term in steps:
			next = steps[last_term]
		else:
			next = 0
		van_eck_seq.append(next)
		if next in last_index:
			steps[next] = n - last_index[next]
		last_index[next] = n
	print(van_eck_seq)	

while True:
	input_num = input("input number of terms: ")
	number = int(input_num)
	start = time.time()
	van_eck_sequence(number)
	end = time.time()
	print("total time = %f" %(end-start))
			
		
      
