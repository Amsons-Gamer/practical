ilist = list(eval(input("enter few numbers using , ")))
ilist.sort() 
mid = len(ilist) // 2
res = (ilist[mid] + ilist[~mid]) / 2
print("Median of list is : " + str(res))