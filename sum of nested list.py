n=[4,5,4,[4,8,7]]
i=0
sum=0
while i<len(n):
    if type(n[i])==type([]):
        j=0
        while j<len(n[i]):
            sum+=n[i][j]
            j+=1
    else:
        sum+=n[i]
    i+=1
print(sum)


a=[8,9,[0,5,[5,9]],8]
i=0
sum=0
while i<len(a):
    if type(a[i])==type([]):
        j=0
        while j<len(a[i]):
            if type(a[i][j])==type([]):
                k=0
                while k<len(a[i][j]):
                    sum=sum+a[i][j][k]
                    k+=1
            else:
                sum+=a[i][j]
            j+=1
    else:
        sum+=a[i]
    i+=1
print(sum)



a=[8,9,[0,5,[4,5,[7]],[5,9]],8]
i=0
sum=0
while i<len(a):
    if type(a[i])==type([]):
        j=0
        while j<len(a[i]):
            if type(a[i][j])==type([]):
                k=0
                while k<len(a[i][j]):
                    if type(a[i][j][k])==type([]):
                        l=0
                        while l<len(a[i][j][k]):
                            sum=sum+a[i][j][k][l]
                            l+= 1
                    else:
                        sum+=a[i][j][k]
                    k+=1
            else:
                sum+=a[i][j]
            j+=1
    else:
        sum+=a[i]
    i+=1
print(sum)

a=[9,[27,[3,5],9],10]
i=0
sum=0
while i<len(a):
    if type(a[i])==type([]):
        j=0
        while j<len(a[i]):
            if type(a[i][j])==type([]):
                k=0
                while k<len(a[i][j]):
                    sum=sum+a[i][j][k]
                    k+=1
            else:
                sum+=a[i][j]
            j+=1
    else:
        sum+=a[i]
    i+=1
print(sum)

