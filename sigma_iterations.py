def find_factors(number):
	divisors_list = []

	# check all the numbers below the square root of the number
	last=1 + int(number ** (1/2))
	for divisor in range(1, last):
		if number % divisor == 0:
			divisor2 = int (number/divisor)
			divisors_list.append(divisor)
			if divisor != divisor2:
				divisors_list.append(divisor2)
	return divisors_list

def sigma(number):
	# get all factors of the number 
	divisors_list = find_factors(number)
	
	# Add up the factors
	sum=0
	for divisor in divisors_list:
		sum += divisor
	return sum

while True:
	input_num = input("input a number: ")
	number = int(input_num)
	next = sigma(number)
	print(number)
	steps = 1
	while next % number != 0:
		print(next)
		next = sigma(next)
		steps += 1
	print(next)
	print("steps =",steps)
