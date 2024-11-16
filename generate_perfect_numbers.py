number=1
while True:
    
    #1.  find the factors
    divisors_list = []
    # check all the numbers below the square root of the number
    last=1 + int(number ** (1/2)) # add 1 because range doesn't include last
    for divisor in range(1, last):
        if number % divisor == 0:
            divisor2 = int (number/divisor)
            divisors_list.append(divisor)
            if divisor != divisor2:
                divisors_list.append(divisor2)
            
    # 2. Add up the factors
    sum=0
    for divisor in divisors_list:
        sum += divisor
    # 3. Check if sum of divisors = number
    if sum == 3*number:
        print( "%d is a perfect number" % number)
    # 4. Try next number
    number += 1
     
