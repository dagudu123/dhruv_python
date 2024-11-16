# Levine sequence
# 2
#  ,#of 2s, # of 1

##2
##1 1
##1 2
##1 1 2
##1 1 2 3
##1 1 1 2 2 3 4
##1 1 1 1 2 2 2 3 3 4 4 5 6 7
##1 1 1 1 1 1 1 2 2 2 2 2 2 3 3 3 3 3 4 4 4 4 5 5 5 5 6 6 6 7 7 7 8 8 9 9 10 10 11 12 13 14



a1=[2]
a2=[]

for r in range(0, 15):
    num=1
    sum=0
    for n in a1[::-1]:
        for i in range(0,n):
            a2.append(num)
            sum += num
        num += 1

    a1=a2
    a2=[]
    print(a1)
    print ("sum=" + str(sum))
