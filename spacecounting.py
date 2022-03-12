def count(a):
    b=a.split()
    i=0
    c=1
    while i<len(b):
        if i%2!=0:
            b.insert(i,c)
            c+=1
        i+=1
    print(b)
count("my name is gudia")