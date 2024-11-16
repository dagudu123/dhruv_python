l = [0, 9, 10 , -1, 20, 10, 23, 7, 99, -62, 457, 81]
while True:

        # 1. Get input number
        input_num = input("input a number: ")
        number= int(input_num)

        found = False
        index = 1
        # find if number exists in list
        for elem in l:
                if elem == number:
                        found = True
                        print("%d is in index %d of the list" % (number, index))
                        break
                index += 1

        if not found:
                print("%d is not in the list" % number)
