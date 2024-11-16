import sys

fib1=1
fib2=1


for i in range(int(sys.argv[1])):
    tmp=fib1+fib2
    fib1=fib2
    fib2=tmp
    print(fib1, fib2/fib1)

