def prime_factors():
    num = int(input("Enter number whose prime factors are to be found\n"))
    factors = []
    prime_factors_list = []
    answer = ""
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            factors.append(i)
    for i in range(len(factors)):
        for j in range(1, (factors[i] // 2) + 1):
            if factors[i] % j == 0 and factors[i] != j and j != 1:
                answer = "No"
                break
            else:
                answer = "Yes"
        if answer == "Yes":
            prime_factors_list.append(factors[i])
    if len(prime_factors_list) > 0:
        print(prime_factors_list)
    else:
        print("The given number is prime number itself")
