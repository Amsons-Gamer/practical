n=int(input('Enter no of rows you want'))
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j, end=' ')
    print()