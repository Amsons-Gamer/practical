import random
n = int(input("enter no of elements you want to have in list"))
l=[]
for i in range(n):
    rd = random.randint(1, 100)
    l.append(rd)
print ("The generated list is:",l)
l.sort()
print("the max of the list is:",l[-1], "and the min of the list is:",l[0])
