how = 4
for row in range(1,how+1):
    for space in range(how-row):
        print(" ",end="")
    for star in range(row*2-1):
        print("*",end="")
    print()
