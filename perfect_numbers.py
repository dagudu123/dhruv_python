while True:
    # 1. Get input number
    input_num = input("input a number: ")
    number= int(input_num)
    divisors_list = []    

    #2.  find the factors
    # check all the numbers below the square root of the number
    last=1 + int(number ** (1/2))
    print (last)
    for divisor in range(1, last):
        if number % divisor == 0:
            divisor2 = int (number/divisor)
            print(divisor, divisor2)
            divisors_list.append(divisor)
            if divisor != divisor2:
                divisors_list.append(divisor2)
            
    # 3. Add up the factors
    sum=0
    for divisor in divisors_list:
        sum += divisor
    print(sum)    
    # 4. Check if sum of divisors = number
    if sum == 2*number:
        print( "%d is a perfect number" % number)
     
    else:
        print( "%d is not a perfect number" % number)
    print("The abundancy index of %d is %f" % (number, sum/number)) 
