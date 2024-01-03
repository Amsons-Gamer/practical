n = int(input("Enter a no to print its Factorial"))
f = 1
i = n
while i > 0:
    f *= i
    i -= 1
print("Factorial of",n,"is",f)