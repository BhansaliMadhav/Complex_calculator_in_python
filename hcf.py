import decimal
import math


def hcf():
    y = ""
    factor_1 = []
    factor_2 = []
    user_input_1 = int(input("Enter first number\n"))
    user_input_2 = int(input("Enter second number\n"))
    for i in range(1, user_input_1 + 1):
        if user_input_1 % i == 0:
            factor_1.append(i)
        else:
            continue
    for j in range(1, user_input_2 + 1):
        if user_input_2 % j == 0:
            factor_2.append(j)
    for i in range(-1, -len(factor_1) - 1, -1):
        for j in range(-1, -len(factor_2) - 1, -1):
            if factor_1[i] == factor_2[j]:
                s = factor_1[i]
                y = "True"
                print("Largest factor is :", s)
                break

        if y == "True":
            break
