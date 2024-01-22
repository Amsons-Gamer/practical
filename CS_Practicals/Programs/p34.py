lst = list(eval(input("enter list of numbers seperated by coma: ")))
n=len(lst) 
s=0
for i in range(n+1):
    s+=i
mean = s/n
print("average is:",mean)