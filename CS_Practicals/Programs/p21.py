string = input("enter a string:")
count = 0
for i in string:
    if i in ['a','e','i','o','u']:
        count+=1
print("no of vowels in the word", string, "is", count)