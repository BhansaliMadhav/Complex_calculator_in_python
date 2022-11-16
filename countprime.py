def count():
    x = int(input("Enter a number upto which you want to find no. of primes : "))
    k = 0
    for i in range(2, x + 1):
        s = 0
        for j in range(1, i + 1):
            if i % j == 0:
                s += 1
        if s == 2:
            print(i,end=", ")
            k += 1
    print("\nTotal no. of primes below ", x, "is ", k)
