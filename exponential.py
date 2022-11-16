import math
import decimal


def exponential():
    user_input_set = input("Enter base, power separated by comma\n")
    user_input = user_input_set.split(",")
    # Condition for base to be e
    if user_input[0] == "e":
        print(f"Your answer is {math.exp(decimal.Decimal(user_input[1]))}")
    # For other bases except "e"
    else:
        print(f"Your answer is {decimal.Decimal(user_input[0]) ** decimal.Decimal(user_input[1])}")