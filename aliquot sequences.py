# find all factors of number
# Return: list of all divisors of number

def find_factors(number):
	divisors_list = []

	# check all the numbers below the square root of the number
	last=1 + int(number ** (1/2))
	#print(last)
	for divisor in range(1, last):
		if number % divisor == 0:
			divisor2 = int (number/divisor)
			#print(divisor, divisor2)
			divisors_list.append(divisor)
			if divisor != divisor2:
				divisors_list.append(divisor2)

	return divisors_list

def aliquot_sum(number):
	# get all factors of the number 
	divisors_list = find_factors(number)
	
	# Add up the factors
	sum=0
	for divisor in divisors_list:
		sum += divisor
	return sum - number


while True:
	# 1. Get input number
	input_num = input("input a number: ")
	number= int(input_num)
	aliquot_set = set()
	print(number)
	
	# Find aliquot sequence of number
	while number != 1:
		next = aliquot_sum(number)
		print(next)
		if next in aliquot_set:
			break
		aliquot_set.add(next)
		number = next
	print("The aliquot sequence of %s has length %d" % (input_num, len(aliquot_set)))	
