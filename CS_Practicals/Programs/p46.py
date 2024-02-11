xnumber = input("Enter a number: ")
sum = 0
number_str = str(number)
for digit_str in number_str:
    digit_int = int(digit_str)
    sum += digit_int
print("The sum of the digits is:", sum)
