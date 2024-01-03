num = int(input("Enter a number: "))
prime = False
if num == 1:
    print(num, "is neither a prime nor a composite number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            prime = True
            break
    if prime:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")