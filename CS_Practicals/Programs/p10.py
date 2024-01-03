n=int(input("Enter number of elements you want to add"))
li=[]
for i in range(n):
    el=int(input("Enter element: "))
    li.append(el)

print("maximum of the list is", max(li))
print("minimum of the list is ", min(li))