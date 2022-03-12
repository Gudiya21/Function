a=[1,32,56,4,]
i=0
m=[]
while i<len(a):
    j=0
    s=""
    b=str(a[i])
    while j<len(b):   
        if b[j]=='1':
            s=s+'one'
        if b[j]=='2':
            s=s+'two '
        if b[j]=='3':
            s=s+'three '
        if b[j]=='4':
            s=s+'four '
        if b[j]=='5':
            s=s+'five '
        if b[j]=='6':
            s=s+'six '
        if b[j]=='7':
            s=s+'seven '
        if a[j]=='8':
            s=s+'eight '
        if a[j]=='9':
            s=s+'nine '
        if a[j]=='10':
            s=s+'ten '
        if a[j]=='0':
            s=s+'zero '
        j+=1
    i+=1
    m.append(s)
print(m)