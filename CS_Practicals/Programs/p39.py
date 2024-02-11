v,c=0,0
word = input("Enter a word")
for i in range(len(word)):
    if word[i] in ['a','e','i','o','u']:
        v+= 1
    else:
        c+=1
print("This word has",v,'vowels and',c,'consonants')