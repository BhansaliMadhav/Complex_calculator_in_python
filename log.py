import math


def log():
    user_input_set = input("Enter number , base separated by comma\n")
    user_input = user_input_set.split(",")
    # condition for log to base e
    if user_input[1] == "e":
        print(f"Your answer is {math.log(float(user_input[0]))}")
    # condition for log to variable base
    else:
        base = user_input[1]
        print(f"Your answer is {math.log10(float(user_input[0])) / math.log10(float(base))}")