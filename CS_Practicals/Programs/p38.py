largest_prime = -1
n =int(input("Enter a number"))
for i in range(n, 0, -1):
    for j in range(2, i): 
        if i % j == 0:
            break
    else:
        largest_prime = i
        break
print("The largest prime number less than", n, "is", largest_prime)