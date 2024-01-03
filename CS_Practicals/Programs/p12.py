#Write a program to print Fibonacci series.
t=int(input("Enter how many terms you want in fibonacchi series"))
a,b=0,1 
print("Fibonacci Series:")
for i in range(t):
    print(a)
    a,b=b,a+b

