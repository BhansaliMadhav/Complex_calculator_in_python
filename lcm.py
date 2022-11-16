import math
import decimal


def lcm():
    user_input_1 = int(input("Enter first number\n"))
    user_input_2 = int(input("Enter second number\n"))
    list_1 = [user_input_2, user_input_1]
    for i in range(max(list_1), (user_input_2 * user_input_1) + 1):
        if i % user_input_1 == 0 and i % user_input_2 == 0:
            print(f"LCM of {user_input_1} and {user_input_2} is {i}")
            break
