def highest(a, b):
    if a > b:
        highest_num = a
    else:
        highest_num = b

    print("The highest number entered is {}".format(highest_num))


def lowest(a, b):
    if a < b:
        lowest_num = a
    else:
        lowest_num = b

    print("The lowest number entered is {}".format(lowest_num))


def multiply(a, b):
    multiplied = a * b
    print("{} times {} = {}".format(a, b, multiplied))


# Main Routine
num_1 = int(input("Enter a number"))
num_2 = int(input("Enter another number"))
highest(num_1, num_2)
lowest(num_1, num_2)
multiply(num_1, num_2)
