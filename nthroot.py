import math
import decimal


def nthroot():
    user_input_set = input("Enter number, which root you want to take(in form of number) separated by comma\n")
    user_input = user_input_set.split(",")
    print(f"Your answer is {decimal.Decimal(user_input[0]) ** (1 / decimal.Decimal(user_input[1]))}")