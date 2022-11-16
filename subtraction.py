import decimal
def subtraction():
    user_input_set = input("Enter two numbers to be subtracted separated by comma\n")
    user_input = user_input_set.split(",")
    print(f"Your answer is {decimal.Decimal(user_input[0]) - decimal.Decimal(user_input[1])}")
