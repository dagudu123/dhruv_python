# question: find the sum of even fibonacci numbers
# under 4 million

fib=[1,1]

# Step 1: generate fibonacci numbers below 4M
while True:
    # generate next fib number
    next = fib[-1] + fib[-2]

    # check end condition
    if next >= 4000000:
        break

    # add element to the list
    fib.append(next)
    

# Step 2: find sum of all even fibonacci numbers < 4M
sum=0
for next in fib:
    if next%2 == 0:
        sum=sum+next

print("sum = %d" %sum)
