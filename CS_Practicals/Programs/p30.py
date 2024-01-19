input_string = input("enter a sentence")
uppercase_count = 0
for char in input_string:
    if char.isupper():
        uppercase_count += 1
print("Uppercase letter =",uppercase_count) 