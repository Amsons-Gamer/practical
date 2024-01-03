n=int(input("Enter a no to check armstrong or not"))
sum_of_cubes = 0
temp = n
remainder = 0
while temp > 0:
    remainder = temp % 10
    sum_of_cubes += remainder ** 3
    temp //= 10
if n == sum_of_cubes:
    print(n,"is an Armstrong number")
else:
    print(n,"is not an Armstrong number")