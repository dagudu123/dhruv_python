while True:
	input_string = input("input a string: ")
	is_a_palindrome = True
	for n in range(0,int(len(input_string)/2)):
		if input_string[n] != input_string[-(n+1)]:
			is_a_palindrome = False
			print(input_string, "is not a palindrome")
			break
	if is_a_palindrome:
		print(input_string, "is a palindrome")
