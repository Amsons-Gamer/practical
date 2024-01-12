string = input('enter a string')
reverse=string[::-1]
if string == reverse:
    print("The given string is palindrome")
else:
    print("The given string is not palindrome")