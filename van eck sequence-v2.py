import time
van_eck_sequence = [0]
start = time.time()
for n in range(1,100000):
	# Find the index of the previous occurence of (n-1)th term
	last_term = van_eck_sequence[n-1] # n-1th term

	found = False
	# find index of the previous occurence of last
	for i in range(n-1, -1, -1):
		if van_eck_sequence[i] == last_term:
			next = n-1-i
			found = True
			break
	if not found:
		next = 0
	van_eck_sequence.append(next)
end = time.time()
print("total time: %f" %(end-start))
print(van_eck_sequence)	
			
                
      
