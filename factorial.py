import decimal


def factorial():
    user_input = input("Enter number whose factorial is to be found\n")
    if decimal.Decimal(user_input) > 0:
        factorial_ = 1
        for i in range(1, int(user_input) + 1):
            factorial_ = decimal.Decimal(factorial_ * i)
        print(factorial_)
    elif int(user_input) == 0:
        print("Factorial of 0 is 1")
    elif int(user_input) < 0:
        print("Factorial of negative numbers in not defined")
