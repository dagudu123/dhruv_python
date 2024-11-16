l = [0, 9, 10 , -1, 20, 10, 23, 7, 99, -62, 457, 81]
while True:

        # 1. Get input number
        input_num = input("input a number: ")
        number= int(input_num)

        found = False
        # find if number exists in list
        for elem in l:
                if elem == number:
                        found = True
                        print("%d is in the list" % number)
                        break
        if not found:
                print("%d is not in the list" % number)
