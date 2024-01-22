lst = list(eval(input("enter list of numbers seperated by , ")))
for i in lst:
    if i%2!=0:
        lst.remove(i)
print('Your list with even numbers is ',lst)