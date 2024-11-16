while True: 
	input_num = input("input a number: ")
	number= int(input_num)
	steps = 0
	while number != 1:
		if number % 2 == 1:
			number = (number*3) + 1
		else:
			number=number/2
		print(int(number))
		steps += 1
	print("steps = ",steps)
