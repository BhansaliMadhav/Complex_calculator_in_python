import math
import decimal


def trigonometric():
    condition = "True"
    user_input_set = input("Enter trigonometric function for eg sin if you want to take sine, angle(in degrees)  separated by comma\n")
    user_input = user_input_set.split(",")

    if user_input[0] == "sin":
        angle_in_radians = decimal.Decimal(math.radians(decimal.Decimal(user_input[1])))
        print(f"Your answer is {round(math.sin(angle_in_radians), 3)}")

    elif user_input[0] == "tan":
        for n in range(10000):
            if float(user_input[1]) == (2 * n + 1) * 90:
                print("Value of odd multiple of pi/2 is infinity")
                condition = "True"
                break
            elif float(user_input[1]) == (2 * n) * 90:
                print("Value of odd multiple of pi is ", 0)
                condition = "True"
                break

        if condition == "False":
            angle_in_radians = math.radians(decimal.Decimal(user_input[1]))
            print(f"Your answer is {round(math.tan(angle_in_radians), 3)}")

    elif user_input[0] == "cos":
        angle_in_radians = math.radians(decimal.Decimal(user_input[1]))
        print(f"Your answer is {round(math.cos(angle_in_radians), 3)}")

