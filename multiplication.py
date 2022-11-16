import decimal


def multiplication():
    user_input_set = input("Enter all the numbers to be multiplied separated by comma\n")
    user_input = user_input_set.split(",")
    num = len(user_input)
    mult = 1
    for i in range(num):
        mult = mult * decimal.Decimal(user_input[i])
    print(f"Your answer is {mult}")