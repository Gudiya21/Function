a=[2,18,14,3,8,7]
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[i]<a[j]:
            k=a[i]
            a[i]=a[j]
            a[j]=k
        j+=1
    i+=1
    print(a)