#0
#1 1 0
#2 2 2 0
#3 2 4 1 1 0
#4 4 4 1 4 0
#5 5 4 1 6 2 1 0
#6 7 5 1 6 3 3 1 0
# ....

# Add 

inv=[]

for iteration in range(0,10):
    i = 0
    elem = inv[i-1]
    row = []
    while elem != 0:
        if i >= len(inv):
            elem = 0
        else:
            elem = inv[i]
        row.append(elem)
        if elem >= len(inv):
            inv.extend([0] * (elem + 1 - len(inv)))
        inv[elem] += 1
        i += 1        

    print (row)
