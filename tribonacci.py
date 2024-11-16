import sys

fib1=1
fib2=2
fib3=2


for i in range(int(sys.argv[1])):

# f1  f2  f3   tmp
# 1   1   2   f1+f2+f3
#    f1   f2    f3
    print(fib1, fib2/fib1)
    tmp=fib1+fib2+fib3
    fib1=fib2
    fib2=fib3
    fib3=tmp



