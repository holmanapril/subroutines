def average_value(a, b, c):
    average = (a + b + c)/3
    print("The average value is {}".format(average))


# Main Routine
num_1 = int(input("Pick a number"))
num_2 = int(input("Pick another number"))
num_3 = int(input("Pick one last number"))
average_value(num_1, num_2, num_3)
