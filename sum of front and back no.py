a=[4,8,9,3,4,6,1,0]
i=0
sum=0
l=[]
while i>-len(a):
    k=0
    while k<len(a):
        sum=a[i-1]+a[k]
        l.append(sum)
        k+=1
        i-=1
i=0
b=[]
while i<len(l):
    if l[i] not in b:
        b.append(l[i])
        
    i+=1
print(b)


