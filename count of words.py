a=['my name is gudia','i have apple']
i=0
b=[]
while i<len(a):
    c=a[i].split()
    i+=1
    b.append(c)
    count=0
    j=0
while j<len(b):
    l=0
    while l<len(b[j]):
        count+=1
        l+=1
    j+=1
print(count)
