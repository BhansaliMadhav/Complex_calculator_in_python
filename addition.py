import decimal


def addition():
    user_input_set = input("Enter all the numbers to be added separated by comma\n")
    user_input = user_input_set.split(",")
    num = len(user_input)
    sum = 0
    for i in range(num):
        sum = sum + decimal.Decimal(user_input[i])
    print(f"Your answer is {sum}")
