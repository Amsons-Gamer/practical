sentence  = input("Enter a sentence")
split = sentence.split()
for i in split:
    if i[0] in ['a','e','i','o','u']:
        print("words that starts with vowel is/are:",i)