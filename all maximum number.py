a = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
i=0
while i<len(a):
    j=0
    max=0
    while j<len(a[i]):
        if a[i][j]>max:
            max=a[i][j]
            
        j+=1
    print(max)
    i+=1


                        