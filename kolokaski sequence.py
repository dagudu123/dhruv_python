import time
while True:
	input_num = input("input number of terms: ")
	k = int(input_num)
	seq = [1,2,2]
	run_index = 2
	run_length = seq[run_index]
	next_term = 1
	start = time.time()
	while len(seq) < k:
		for i in range(0,run_length):
			seq.append(next_term)
		run_index += 1
		run_length = seq[run_index]
		last_term = seq[-1]
		next_term = (1 if last_term == 2 else 2)
	end = time.time()
	print(seq)
	print("total time =", end-start)

