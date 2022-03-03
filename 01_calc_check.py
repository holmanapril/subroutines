def calculate(question_1, question_2, math, choices):
    num_1 = int(input(question_1))
    num_2 = int(input(question_2))
    valid = False
    while not valid:
        operator = input(math)
        if operator in choices:
            if operator == "-":
                answer = num_1 - num_2
                valid = True
            elif operator == "+":
                answer = num_1 + num_2
                valid = True
            elif operator == "*":
                answer = num_1 * num_2
                valid = True
            elif operator == "/":
                answer = num_1 / num_2
                valid = True
        else:
            print("Please enter a valid input")

        print("The answer to your question\n{} {} {} equals {}".format(num_1, operator, num_2, answer))


# Main Routine
calculate("Enter the first number", "Enter the second number", "Enter the operator(+, - , *, /)", ["+", "-", "*", "/"])
