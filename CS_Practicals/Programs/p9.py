n=int(input("Enter no of terms you want to take and print its sum "))
count=0
print("Numbers are- ", end="")
for i in range(1,n+1):
    print(i, end=" ")
    count+=i

print("\n their count is",count)
