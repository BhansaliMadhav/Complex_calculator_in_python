import math
import decimal


def inversetrigonometric():
    user_input_set = input(
        "Enter inverse trigonometric function for eg sin if you want to take sin inverse, value  separated by comma\n")
    user_input = user_input_set.split(",")
    # Condition for sin calculation
    if user_input[0] == "sin":
        angle_in_rads = math.asin(float(user_input[1]))
        angle_in_deg = math.degrees(angle_in_rads)
        print(f"Your answer is {angle_in_deg}")

    # Condition for tan calculation
    elif user_input[0] == "tan":
        angle_in_rads = math.atan(float(user_input[1]))
        angle_in_deg = math.degrees(angle_in_rads)
        print(f"Your answer is {angle_in_deg}")

    # Condition for cos calculation
    elif user_input[0] == "cos":
        angle_in_rads = math.acos(float(user_input[1]))
        angle_in_deg = math.degrees(angle_in_rads)
        print(f"Your answer is {angle_in_deg}")
